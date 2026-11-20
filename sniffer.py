from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = "OTHER"
        ports = ""

        if TCP in packet:
            proto = "TCP"
            ports = f"{packet[TCP].sport} -> {packet[TCP].dport}"
        elif UDP in packet:
            proto = "UDP"
            ports = f"{packet[UDP].sport} -> {packet[UDP].dport}"
        elif ICMP in packet:
            proto = "ICMP"

        print(f"[{proto}] {src_ip} -> {dst_ip} {ports}", flush=True)

        if Raw in packet:
            payload = packet[Raw].load.decode(errors="ignore").strip()
            if payload:
                print(f"    Payload: {payload[:100]}", flush=True)


if __name__ == "__main__":
    print("Starting packet capture... Press Ctrl+C to stop.", flush=True)
    try:
        sniff(prn=analyze_packet, store=False)
    except KeyboardInterrupt:
        print("\nPacket capture stopped.", flush=True)

# Basic Network Sniffer 

A lightweight Python packet sniffer built with **Scapy** that captures live network traffic, dissects protocol headers across network and transport layers, and extracts readable application-layer payloads.

---

## Features

- Captures live packets without storing them in memory (`store=False`).
- Extracts **Source IP** and **Destination IP** addresses from IPv4 headers.
- Identifies transport and network protocols (**TCP**, **UDP**, **ICMP**, or **OTHER**).
- Displays **Source and Destination Ports** for TCP and UDP traffic.
- Decodes and previews readable **Raw Payloads** (first 100 characters).

---

## How Protocol Dissection Works

Network traffic is encapsulated in layers following the OSI / TCP-IP model. When Scapy captures a raw frame from the network interface, it parses each layer sequentially from outer header to inner payload:

1. **IP Layer (`IP in packet`)**
   - Filters for IPv4 traffic and extracts `packet[IP].src` (source IP) and `packet[IP].dst` (destination IP).
2. **Transport & Control Layers (`TCP`, `UDP`, `ICMP`)**
   - **TCP (`TCP in packet`):** Connection-oriented traffic (e.g., HTTP on port 80, HTTPS on port 443). Extracts `sport` (source port) and `dport` (destination port).
   - **UDP (`UDP in packet`):** Connectionless traffic (e.g., DNS queries on port 53). Extracts `sport` and `dport`.
   - **ICMP (`ICMP in packet`):** Network diagnostic messages (e.g., Echo Request/Reply from `ping`). Does not use ports.
3. **Application Payload (`Raw in packet`)**
   - Extracts raw bytes after transport headers (`packet[Raw].load`), decodes them to readable text while ignoring non-UTF8 bytes (`errors="ignore"`), and prints the first 100 characters.

---

## Setup & Usage (Kali Linux)

### 1. Clone and Install Dependencies
```bash
git clone https://github.com/raisulfahad/CodeAlpha_Basic_Network_Sniffer.git
cd CodeAlpha_Basic_Network_Sniffer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Sniffer
Packet capture requires root privileges to put the network interface into promiscuous mode:
```bash
sudo python sniffer.py
```

### 3. Generate Sample Traffic
In a second terminal:
```bash
ping -c 4 8.8.8.8
curl http://example.com
```

### Sample Output
```text
Starting packet capture... Press Ctrl+C to stop.
[ICMP] 192.168.1.15 -> 8.8.8.8 
[ICMP] 8.8.8.8 -> 192.168.1.15 
[UDP] 192.168.1.15 -> 8.8.8.8 51422 -> 53
[TCP] 192.168.1.15 -> 93.184.215.14 48910 -> 80
    Payload: GET / HTTP/1.1
Host: example.com
User-Agent: curl/8.7.1
Accept: */*
```



Created by [MD Raisul Fahad](https://github.com/raisul06) ·

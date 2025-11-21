#!/usr/bin/env python3
"""
Sample Traffic Generator
Create test PCAP files for demonstration
"""

from scapy.all import *
import random

def generate_sample_pcap():
    """Generate a sample PCAP file for testing"""
    packets = []
    
    # Generate normal web traffic
    for i in range(50):
        packet = IP(src="192.168.1.10", dst="93.184.216.34") / TCP(dport=80)  # example.com
        packets.append(packet)
    
    # Generate suspicious traffic (port scan)
    for port in [21, 22, 23, 25, 53, 80, 443, 3389]:
        packet = IP(src="192.168.1.100", dst="192.168.1.50") / TCP(dport=port, flags="S")
        packets.append(packet)
    
    # Generate DNS queries
    for query in ["google.com", "github.com", "example.org"]:
        packet = IP(src="192.168.1.10", dst="8.8.8.8") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=query))
        packets.append(packet)
    
    # Save to file
    wrpcap("samples/example.pcap", packets)
    print("✅ Sample PCAP generated: samples/example.pcap")

if __name__ == "__main__":
    generate_sample_pcap()
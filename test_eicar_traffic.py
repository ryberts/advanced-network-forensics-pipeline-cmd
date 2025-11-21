from scapy.all import *
import base64

# EICAR test string
eicar_string = r'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'

# Create packets simulating EICAR file transfer
packets = []

# Simulate HTTP download containing EICAR
http_request = IP(src="192.168.1.100", dst="93.184.216.34") / TCP(dport=80, sport=54321) / \
               Raw(load="GET /eicar_com.txt HTTP/1.1\r\nHost: example.com\r\n\r\n")
packets.append(http_request)

# Simulate HTTP response with EICAR content
http_response = IP(src="93.184.216.34", dst="192.168.1.100") / TCP(dport=54321, sport=80) / \
                Raw(load="HTTP/1.1 200 OK\r\nContent-Length: 68\r\n\r\n" + eicar_string)
packets.append(http_response)

# Simulate FTP transfer with EICAR
ftp_data = IP(src="192.168.1.100", dst="203.0.113.10") / TCP(dport=21) / \
           Raw(load="STOR eicar_com.txt\r\n")
packets.append(ftp_data)

# Add some normal traffic for context
for i in range(10):
    packets.append(IP(src=f"192.168.1.{i+10}", dst="8.8.8.8") / TCP(dport=53))
    packets.append(IP(src=f"192.168.1.{i+10}", dst="1.1.1.1") / TCP(dport=80))

# Save the PCAP
wrpcap("samples/eicar_test.pcap", packets)
print("✅ Created EICAR test traffic: samples/eicar_test.pcap")

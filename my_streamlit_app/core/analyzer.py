#!/usr/bin/env python3
"""
Packet Analysis Engine
Robust PCAP parsing and analysis
"""

import pyshark
import logging
from collections import Counter, defaultdict

class PacketAnalyzer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def analyze(self, pcap_file, max_packets=50000):
        """Analyze PCAP file and extract key metrics"""
        self.logger.info(f"Analyzing {pcap_file}...")
        
        analysis = {
            'total_packets': 0,
            'protocols': Counter(),
            'conversations': Counter(),
            'ports': Counter(),
            'packet_sizes': [],
            'timestamps': [],
            'dns_queries': [],
            'http_requests': [],
            'suspicious_activity': []
        }
        
        try:
            cap = pyshark.FileCapture(pcap_file, display_filter='ip')
            
            for packet in cap:
                if analysis['total_packets'] >= max_packets:
                    break
                    
                analysis['total_packets'] += 1
                
                # Basic packet information
                if hasattr(packet, 'ip'):
                    src_ip = packet.ip.src
                    dst_ip = packet.ip.dst
                    
                    # Track conversations
                    conv = f"{src_ip} -> {dst_ip}"
                    analysis['conversations'][conv] += 1
                    
                    # Protocol analysis
                    if hasattr(packet, 'transport_layer'):
                        analysis['protocols'][packet.transport_layer] += 1
                    
                    # Port analysis
                    if hasattr(packet, 'tcp'):
                        analysis['ports'][f"tcp/{packet.tcp.dstport}"] += 1
                    elif hasattr(packet, 'udp'):
                        analysis['ports'][f"udp/{packet.udp.dstport}"] += 1
                
                # DNS analysis
                if hasattr(packet, 'dns') and hasattr(packet.dns, 'qry_name'):
                    analysis['dns_queries'].append({
                        'query': packet.dns.qry_name,
                        'src_ip': packet.ip.src if hasattr(packet, 'ip') else 'Unknown'
                    })
                
                # HTTP analysis
                if hasattr(packet, 'http'):
                    if hasattr(packet.http, 'request_uri'):
                        analysis['http_requests'].append({
                            'method': getattr(packet.http, 'request_method', 'GET'),
                            'uri': packet.http.request_uri,
                            'host': getattr(packet.http, 'host', 'Unknown')
                        })
            
            cap.close()
            self.logger.info(f"Analyzed {analysis['total_packets']} packets")
            
        except Exception as e:
            self.logger.error(f"Analysis error: {str(e)}")
            raise
        
        return analysis
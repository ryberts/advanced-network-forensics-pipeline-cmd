#!/usr/bin/env python3
"""
Advanced Network Forensics Pipeline
Professional-grade network traffic analysis and threat detection
"""

import argparse
import logging
import os
import sys
import time
from datetime import datetime

# Import core modules
from core.analyzer import PacketAnalyzer
from core.detector import ThreatDetector
from core.reporter import ReportGenerator

def setup_logging():
    """Configure professional logging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('forensics.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)

def print_banner():
    """Display professional banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║              ADVANCED NETWORK FORENSICS PIPELINE            ║
║                     Production Ready v1.0                   ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def main():
    print_banner()
    logger = setup_logging()
    
    parser = argparse.ArgumentParser(description='Network Forensics Pipeline')
    parser.add_argument('--file', '-f', required=True, help='PCAP file to analyze')
    parser.add_argument('--output', '-o', default='reports', help='Output directory')
    parser.add_argument('--quick', action='store_true', help='Quick analysis mode')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.file):
        logger.error(f"PCAP file not found: {args.file}")
        sys.exit(1)
    
    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"{args.output}/analysis_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        logger.info(f"Starting analysis of: {args.file}")
        start_time = time.time()
        
        # Phase 1: Packet Analysis
        logger.info("Phase 1: Analyzing network packets...")
        analyzer = PacketAnalyzer()
        packet_data = analyzer.analyze(args.file)
        
        # Phase 2: Threat Detection
        logger.info("Phase 2: Detecting security threats...")
        detector = ThreatDetector()
        threats = detector.analyze(packet_data)
        
        # Phase 3: Report Generation
        logger.info("Phase 3: Generating reports...")
        reporter = ReportGenerator()
        report_path = reporter.generate(packet_data, threats, output_dir)
        
        analysis_time = time.time() - start_time
        
        # Print summary
        print(f"\n{'='*50}")
        print("ANALYSIS COMPLETE")
        print(f"{'='*50}")
        print(f"📁 Reports: {report_path}")
        print(f"⏱️  Time: {analysis_time:.2f}s")
        print(f"📦 Packets: {packet_data['total_packets']:,}")
        print(f"🔍 Threats: {threats['summary']['total']}")
        print(f"   • High: {threats['summary']['high']}")
        print(f"   • Medium: {threats['summary']['medium']}")
        
        if threats['high_severity']:
            print(f"\n⚠️  HIGH PRIORITY ALERTS:")
            for threat in threats['high_severity'][:3]:
                print(f"   • {threat['type']}: {threat['description']}")
                
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
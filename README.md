# 🔍 Advanced Network Forensics Pipeline

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> Enterprise-grade network forensics and threat detection pipeline. BTL1-aligned, production-ready.

## 🚀 Features

- **Automated PCAP Analysis**: Extract and analyze network traffic patterns
- **Multi-Stage Threat Detection**: Identify reconnaissance, exploitation, lateral movement, data exfiltration
- **Professional Reporting**: Generate HTML, JSON, and executive summary reports
- **Network Visualization**: Create topology maps and statistical charts
- **BTL1 Ready**: Perfect for certification preparation and portfolio projects

## 📦 Quick Start

### Prerequisites
- Python 3.8+
- Ubuntu/Linux (recommended) or Windows with WSL

### Installation & Run (3 commands)

```bash
# 1. Clone and setup
git clone https://github.com/yourusername/network-forensics-pipeline
cd network-forensics-pipeline

# 2. Install dependencies (30 seconds)
./setup.sh

# 3. Run analysis on sample data
python forensics_pipeline.py --file samples/example.pcap
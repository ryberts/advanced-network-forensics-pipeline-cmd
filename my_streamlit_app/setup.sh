#!/bin/bash
echo "🔧 Setting up Network Forensics Pipeline..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install system dependencies
sudo apt install -y python3 python3-pip wireshark tshark

# Create virtual environment
python3 -m venv forensics_env
source forensics_env/bin/activate

# Install Python packages
pip install -r requirements.txt

# Create sample data directory
mkdir -p samples
echo "✅ Setup complete! Activate with: source forensics_env/bin/activate"
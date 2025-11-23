
<a id="readme-top"></a>

<!-- PROJECT -->

<br />
<div align="center">

<h1 align="center">🛡️Advanced Network Forensics Pipeline CLI Version</h1>

  <p align="center">
    Enterprise-grade network forensics and threat detection pipeline. BTL1-aligned, production-ready.</br>
    Related Project - use this in <a href="https://github.com/ryberts/advanced-network-forensics-pipeline-cmd/">PCAP Attack Simulation Generator</a>
    <br />
    </a>
    &middot;
    <a href="https://github.com/ryberts/advanced-network-forensics-pipeline-cmd/issues">Report Bug or Request a Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS a dropdown hidden TOC -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#live-demo">Live Demo</a>
      <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#run-commands">Run Commands</a></li>
      </ul>
    </li>
    <li><a href="#usage-and-output">Usage & Output</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#complimentary-app">Complimentary App to Use</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT **screenshot is optional -->

## Live Demo

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ryberts/advanced-network-forensics-pipeline-cmd)

## About The Project

- **Automated PCAP Analysis**: Extract and analyze network traffic patterns
- **Multi-Stage Threat Detection**: Identify reconnaissance, exploitation, lateral movement, data exfiltration
- **Professional Reporting**: Generate HTML, JSON, and executive summary reports
- **Network Visualization**: Create topology maps and statistical charts
- **BTL1 Ready**: Perfect for certification preparation and portfolio projects

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

#### Run Commands

```bash
# 1. choose from the sample\ pcal files or Just run

python forensics_pipeline.py --file samples/example.pcap --verbose

# 2. If you are running this locally, then you must activate the venv:

source forensics_env/bin/activate
```

#### Prerequisites 

(not needed if you run this in codespaces via repo link)
- Python 3.8+
- Ubuntu/Linux (recommended) or Windows with WSL


  
<!-- USAGE -->

## Usage and Output

   ```bash
    python forensics_pipeline.py --file samples/suspicious.pcap --verbose
   ```

[![Sample description of sceenshot][product-screenshot1]](https://example.com)
#### Output - 3 report files in json, txt and html
[![Sample description of sceenshot][product-report1]](https://example.com)
#### Sample html report file
[![Sample description of sceenshot][product-report2]](https://example.com)

A clean looking professional report file

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built

<a id="built-with"></a>

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

<!-- COMPLIMENTARY APP -->

## Complimentary App
If you need to generate a sample test PCAP file to test:

<li>Port Scanning → Connection rate alerts
<li>Data Exfiltration → Volume threshold alerts
<li>DNS Tunneling → Query pattern detection
<li>Suspicious Ports → Known port database matches
<li>Lateral Movement → Internal protocol analysis
<br>

#### Go to this Repo - <a href="https://github.com/ryberts/pcap-attack-generator">PCAP Attack Simulation Generator</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

 [![LinkedIn][linkedin-shield]][linkedin-url]  

email: ryanbertulfo@gmail.com

Project Link: [Click Here!](https://github.com/ryberts/advanced-network-forensics-pipeline-cmd)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/Ryan_Bertulfo-LinkedIn-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNMCAwdjI0aDI0di0yNGgtMjR6bTggMTloLTN2LTExaDN2MTF6bS0xLjUtMTIuMjY4Yy0uOTY2IDAtMS43NS0uNzktMS43NS0xLjc2NHMuNzg0LTEuNzY0IDEuNzUtMS43NjQgMS43NS43OSAxLjc1IDEuNzY0LS43ODMgMS43NjQtMS43NSAxLjc2NHptMTMuNSAxMi4yNjhoLTN2LTUuNjA0YzAtMy4zNjgtNC0zLjExMy00IDB2NS42MDRoLTN2LTExaDN2MS43NjVjMS4zOTctMi41ODYgNy0yLjc3NyA3IDIuNDc2djYuNzU5eiIvPjwvc3ZnPg==

[linkedin-url]: https://www.linkedin.com/in/ryberts/


[product-screenshot]: https://i.imgur.com/xBmlS3x.jpeg
[product-screenshot1]: https://i.imgur.com/spdFcTy.png
[product-report1]: https://i.imgur.com/DjtFogZ.png
[product-report2]: https://i.imgur.com/iEzdozv.png





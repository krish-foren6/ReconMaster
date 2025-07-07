# ReconMaster
ReconMaster – Automated Reconnaissance Toolkit  built for Bug Bounty and Pentesting

# ReconMaster - All-in-One Reconnaissance Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## Overview

**ReconMaster** is a powerful, easy-to-use, and modular reconnaissance tool designed for penetration testers and security researchers.  
It automates and consolidates multiple recon and scanning tools into a single command-line interface, simplifying your bug bounty and pentesting workflow.

Built with Python, ReconMaster integrates popular tools like `nmap`, `amass`, `assetfinder`, `sqlmap`, `gobuster`, and many more — all accessible via a clean menu-driven interface.

---

## Features

- **Modular Design:** Choose from various reconnaissance categories such as Subdomain Enumeration, DNS Recon, Vulnerability Scanning, and Technology Stack Detection.
- **Tool Integration:** Seamlessly runs numerous security tools installed on your system with easy argument passing.
- **Output Saving:** Option to save output in `.txt` or `.html` formats for future reference.
- **User-Friendly UI:** Beautiful ASCII banner and colored outputs for enhanced usability.
- **Extensible:** Add more tools easily by updating the configuration.

---

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Required Python libraries:
  ```bash
  pip install colorama rich pyfiglet
  
**###Clone the Repository:**
git clone https://github.com/yourusername/ReconMaster.git
cd ReconMaster
**###Run the Tool**
python3 reconmaster.py

---

**###Usage**

1. Select Recon Category: Choose from Subdomain Enumeration, DNS Recon, Vulnerability Scanning, or Tech Stack Detection.

2. Select Tool: Pick the tool you want to run within the chosen category.

3. View Help: See the tool’s help message to understand command-line arguments.

4. Enter Command Arguments: Input the full command-line arguments you want to pass to the tool.

5. Execute and Save Output: Run the tool and optionally save its output as .txt or .html.

--- 

**Supported Tools & Categories**

| Category                   | Tools Included                                 |
| -------------------------- | ---------------------------------------------- |
| **Subdomain Enumeration**  | assetfinder, amass, subfinder, sublist3r       |
| **DNS Recon**              | dnsdumpster, whois, dig                        |
| **Vulnerability Scanning** | nmap, sqlmap, dirsearch, gobuster, dirb, nikto |
| **Tech Stack Detection**   | whatweb, webanalyze                            |


---

**License**
This project is licensed under the MIT License — see the [MIT LICENSE](./LICENSE) file for details.

**Contact**
Built by: Krish_foren6
Feel free to reach out for questions or suggestions!

GitHub: https://github.com/krish-foren6

Email: kg646233@gmail.com





# Simple-Auto-Recon
A simple automated reconissance tool configured in python by cyberpands.

---
# Description
This tool is designed for everyone in the cybersecurity field who gets tired of inputting commands every now and then. With the use of ping, whois, dig, traceroute, and nmap aggressive scan, this tools will auto recon on the host. I have been using this fantastic cheat-sheet on [technoctf.in](https://technoctf.in/) offered by Archit Vats for my reference.

---
# Working
This tools performs 4 commands

### 1. Ping Scan - It checks whether the host is alive or not. 
>```Command: ping -c 3 [host or IP]```

### 2. Whois Scan
>```Command: whois [host or IP]```

### 3. Dig Scan
>```Command: dig [host or IP]```

### 4. Traceroute Scan
>```Command: traceroute [host or IP]```

### 5. Nmap Scan
>```Command: nmap -A --script=vuln [host or IP]```
---
# Requirements
Install whois, dig,traceroute and nmap

Commands:

    sudo apt-get install whois

    sudo apt-get install dnsutils

    sudo apt-get install traceroute

    sudo apt-get install nmap
---
# Usage
>```python3 auto_recon.py [host or IP]```
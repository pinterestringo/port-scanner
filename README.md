# Port Scanner 🔍

## Overview
A command-line port scanner built in Python that checks which ports are 
open on a given host. 

> ⚠️ **Note:** This is a personal learning project built to explore networking 
> and cybersecurity concepts. Only scan hosts you own or have explicit 
> permission to scan. Unauthorized port scanning is illegal!

## How It Works
Every computer has up to 65,535 ports. Each one a potential doorway for 
network traffic. This tool attempts to connect to each port in a given range 
and reports which ones are open. Open ports reveal what services are running 
on a machine, which is why port scanning is a foundational step in both 
ethical hacking and network security auditing.

## How to Run
```bash
python3 port_scanner.py
```

## Example Output
```
Host:   127.0.0.1
Ports:  1 - 100

  [OPEN]   Port 22
  [OPEN]   Port 80
  [closed] Port 443
  ...

Scan complete. 2 open port(s) found.
```

## Built With
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## What I Learned
- How ports and network sockets work
- Using Python's socket library for low-level network communication
- How port scanning is used in real-world ethical hacking and security audits
- The importance of responsible, legal, and ethical use of security tools

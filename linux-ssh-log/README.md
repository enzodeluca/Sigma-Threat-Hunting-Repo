# Automated SSH Brute-Force Log Parser & Detector

## Project Overview
This project is a lightweight, native Python security utility designed to parse Linux system authentication logs (`auth.log`/`secure`). It automates the detection of brute-force attacks by isolating malicious IP addresses, tracking failed login attempts, and triggering automated mitigation alerts when configured thresholds are exceeded.

## MITRE ATT&CK Mapping
- **Tactic:** Credential Access (TA0006)
- **Technique:** Brute Force: Password Guessing (T1110.001)
- **Log Telemetry Analyzed:** Linux Syslog / SSH Daemon (`sshd`)

## Core Features
- **Log Parsing & Normalization:** Ingests raw unstructured text data from Linux SSH daemon (`sshd`) logs.
- **Threat Isolation:** Extracted target variables (Timestamp, Target User, Source IP) from failed connection events.
- **Analytical Metrics:** Uses Python data structures to calculate the exact frequency of attacks per unique IP address.
- **Automated Mitigation Logic:** Features an alerting threshold that flags critical threats for firewall containment (simulating Fail2Ban behavior).

## Technical Skills Demonstrated
- **Languages:** Python 3
- **Operating Systems:** Linux Core Administration (Log Triage, CLI File Management)
- **Security Concepts:** Log Analysis, Brute-Force Detection, Automated Incident Response

## How It Works
1. Run `python3 genLogs.py` to simulate live corporate server log traffic.
2. Run `python3 logReview.py` to parse the telemetry, analyze the threat, and view the automated containment report.

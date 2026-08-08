# ThreatIntel-SOAR-Automation
## Project Overview
This project addresses a critical operational bottleneck in Security Operations Centers (SOC): the manual triage of Indicators of Compromise (IoCs). This repository contains a production-ready Python automation engine that ingests suspicious network logs, communicates asynchronously with global threat evaluation APIs (AbuseIPDB), analyzes raw risk variables, and outputs structured intelligence matrix reports.

## System Workflow & Architecture
- **Development Language**: Python 3.x
- **Target APIs**: AbuseIPDB V2 API Engine
- **Data Input Vector**: Native Python Arrays / Dynamic Text File Feeds
- **Data Output Channel**: Comma-Separated Values (CSV) Metric Matrix

## Core Logic & Functional Capabilities
The script iterates through configured IPv4 targets, constructs authenticated REST API requests, and dynamically parses JSON payloads down to critical metrics:
- **Abuse Confidence Score**: Mathematical probability of malicious intent.
- **Geographic Context**: Identification of country origin codes.
- **Reporting Metrics**: Volume of historic security blocks registered against the host.

---
*The complete automation engine and a sample enriched report artifact are hosted natively within this repository files.*

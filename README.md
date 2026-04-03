# IP Reputation Checker

A simple Python tool that checks the reputation of an IP address using the AbuseIPDB API and generates a colored terminal output + Markdown report.

---

## Features

* Check IP reputation (AbuseIPDB)
* Color-coded risk output (Low / Medium / High)
* Generates `report.md` with full analysis
* Basic input validation

---

## Requirements

* Python 3.x
* `requests`

Install dependencies:

```bash
pip install requests
```

---

## Setup

Set your API key as an environment variable:

```bash
export ABUSEIPDB_API_KEY="your_api_key_here"
```

If you don't have one, get it from [AbuseIPDB](https://www.abuseipdb.com/check/43.243.95.36) after signing up.

---

## Usage

```bash
python main.py <IP_ADDRESS>
```

Example:

```bash
python main.py 8.8.8.8
```

---

## Output

* Terminal:

  * IP details
  * Abuse score
  * Risk classification
```
====== IP Reputation Report ======
IP Address:              172.66.148.78
Abuse Score:             0
Risk Level:              LOW
Country:                 US
ISP:                     Cloudflare, Inc.
Domain:                  cloudflare.com
Total Reports:           0
Last Reported:           None
==================================

[+] Report saved to report.md
```

* File:

  * `report.md` → structured investigation report


---

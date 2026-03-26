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

* File:

  * `report.md` → structured investigation report

---

## Use Case

This tool simulates basic threat intelligence enrichment used in:

* SOC analysis
* Log investigation
* Incident response

---

## Notes

* Do NOT hardcode your API key
* Add `.env` or environment variables for security
* Respect API rate limits

---

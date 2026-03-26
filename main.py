import requests
import json
import sys
import os
from datetime import datetime

# Colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
RESET = '\033[0m'

# Check args
if len(sys.argv) != 2:
    print(f"{RED}[ERROR]{RESET} Usage: python script.py <IP>")
    sys.exit(1)

IP = sys.argv[1]

# API key 
API_KEY = os.getenv("ABUSEIPDB_API_KEY")
if not API_KEY:
    print(f"{RED}[ERROR]{RESET} Missing API key. Set ABUSEIPDB_API_KEY environment variable.")
    sys.exit(1)

# API endpoint
url = "https://api.abuseipdb.com/api/v2/check"

headers = {
    "Accept": "application/json",
    "Key": API_KEY
}

params = {
    "ipAddress": IP,
    "maxAgeInDays": 90,
    "verbose": ""
}

try:
    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()["data"]

except requests.exceptions.RequestException as e:
    print(f"{RED}[ERROR]{RESET} Request failed: {e}")
    sys.exit(1)

# Extract values
score = data.get('abuseConfidenceScore', 0)
country = data.get('countryCode')
isp = data.get('isp')
domain = data.get('domain')
reports = data.get('totalReports')
last_report = data.get('lastReportedAt')

# Risk classification
if score <= 25:
    risk_color = GREEN
    risk_level = "LOW"
elif score <= 75:
    risk_color = YELLOW
    risk_level = "MEDIUM"
else:
    risk_color = RED
    risk_level = "HIGH"

# Terminal Output
print(f"\n{CYAN}====== IP Reputation Report ======{RESET}")
print(f"IP Address:              {IP}")
print(f"Abuse Score:             {risk_color}{score}{RESET}")
print(f"Risk Level:              {risk_color}{risk_level}{RESET}")
print(f"Country:                 {country}")
print(f"ISP:                     {isp}")
print(f"Domain:                  {domain}")
print(f"Total Reports:           {reports}")
print(f"Last Reported:           {last_report}")
print(f"{CYAN}=================================={RESET}\n")

# MD Report
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

md_content = f"""# IP Reputation Report

## Summary
- **IP Address:** `{IP}`
- **Check Time:** {timestamp}

## Risk Assessment
- **Abuse Confidence Score:** {score}
- **Risk Level:** {risk_level}

## Network Information
- **Country:** {country}
- **ISP:** {isp}
- **Domain:** {domain}

## Reports
- **Total Reports:** {reports}
- **Last Reported At:** {last_report}

## Analyst Notes
This IP has been classified as **{risk_level} risk** based on AbuseIPDB data.

### Interpretation:
- LOW → Likely benign or minimal reports
- MEDIUM → Suspicious, requires investigation
- HIGH → Likely malicious (scanner, bot, attacker)

## Recommended Actions
"""

# Add recommendations dynamically
if risk_level == "HIGH":
    md_content += "- Block this IP at firewall level\n- Investigate logs for activity\n- Check lateral movement attempts\n"
elif risk_level == "MEDIUM":
    md_content += "- Monitor activity\n- Correlate with logs\n- Consider temporary block\n"
else:
    md_content += "- No immediate action required\n- Continue monitoring\n"

# Write file
with open("report.md", "w") as f:
    f.write(md_content)

print(f"{GREEN}[+] Report saved to report.md{RESET}")

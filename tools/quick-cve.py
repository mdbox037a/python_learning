import requests
import sys
import os
import json
import nvdlib
from dotenv import load_dotenv


load_dotenv()

cve_id = ""
ubu_prio = ""
nvd_severity = ""
headers = {"user-agent": "matthew box/quick-cve.py (github.com/mdbox037a)"}
ubu_url = "https://ubuntu.com/security/cves"
ubu_params = {"cve_id": cve_id}


print(
    "NOTICE: This product uses the NVD API but is not endorsed or certified by the NVD."
)

print(f"{'CVE':<15}| Ubuntu Priority | NVD Severity")
print("===============================================")

for line in sys.stdin:
    cve_id = line.strip()

    if cve_id:
        try:
            target_url = f"https://ubuntu.com/security/cves/{cve_id.upper()}.json"

            ubusec_data = requests.get(target_url, headers=headers, timeout=30)

            if ubusec_data.status_code == 200:
                data = ubusec_data.json()
                ubu_prio = data.get("priority", "N/A").upper()
        except requests.RequestException:
            ubu_prio = "error"
        except requests.Timeout:
            ubu_prio = "timeout"

        try:
            nvd_api_key = os.getenv("NVD_API_KEY")
            if not nvd_api_key:
                raise ValueError("API key not found - check the .env file.")

            nvd_data = nvdlib.searchCVE(
                cveId=cve_id.upper(), key=nvd_api_key, delay=0.6
            )
            if nvd_data:
                cve = nvd_data[0]
                nvd_severity = cve.score[2]
        except Exception as e:
            nvd_severity = "error"
            print(e)

    print(f"{cve_id.upper():<15}: {ubu_prio:<16}: {nvd_severity:<10}")

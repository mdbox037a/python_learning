import sys
import re
import requests


def get_cve_fixes(cve_id):
    url = f"https://api.osv.dev/v1/vulns/{cve_id}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None, f"Not found (HTTP {response.status_code})"

        data = response.json()
        fixed_versions = set()

        for affected in data.get("affected", []):
            for r in affected.get("ranges", []):
                for event in r.get("events", []):
                    if "fixed" in event:
                        fixed_versions.add(event["fixed"])

        return sorted(list(fixed_versions)), None
    except requests.RequestException as e:
        return None, f"Request failed: {e}"


def main():
    input_text = sys.stdin.read()

    # Extract matches and preserve exact input order while deduplicating
    raw_matches = re.findall(r"CVE-\d{4}-\d+", input_text, re.IGNORECASE)
    unique_cves = list(dict.fromkeys([cve.upper() for cve in raw_matches]))

    if not unique_cves:
        print("Error: No CVE patterns detected in stdin input.", file=sys.stderr)
        sys.exit(1)

    for cve in unique_cves:
        fixes, error = get_cve_fixes(cve)

        print(f"{cve}:")
        if error:
            print(f"  - {error}")
        elif fixes:
            for version in fixes:
                print(f"  - Fixed in: {version}")
        else:
            print("  - No fix information found")


if __name__ == "__main__":
    main()

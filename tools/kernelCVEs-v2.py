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
    # Read all piped standard input
    input_text = sys.stdin.read()

    # Extract all CVE IDs (handles mixed text, multiline, or spaces)
    cve_matches = set(re.findall(r"CVE-\d{4}-\d+", input_text, re.IGNORECASE))

    if not cve_matches:
        print("Error: No CVE patterns detected in stdin input.", file=sys.stderr)
        sys.exit(1)

    for cve in sorted(cve_matches, reverse=True):
        cve_upper = cve.upper()
        fixes, error = get_cve_fixes(cve_upper)

        print(f"{cve_upper}:")
        if error:
            print(f"  - {error}")
        elif fixes:
            for version in fixes:
                print(f"  - Fixed in: {version}")
        else:
            print("  - No fix information found")


if __name__ == "__main__":
    main()

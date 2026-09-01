import requests


def batch_get_kernel_fixes(cve_list):
    summary = {}

    for cve in cve_list:
        url = f"https://api.osv.dev/v1/vulns/{cve.strip()}"
        response = requests.get(url)

        if response.status_code != 200:
            summary[cve] = {"error": "CVE not found"}
            continue

        data = response.json()
        fixed_versions = set()

        # Parse affected ranges for fixed versions (tags or commit SHAs)
        for affected in data.get("affected", []):
            for r in affected.get("ranges", []):
                for event in r.get("events", []):
                    if "fixed" in event:
                        fixed_versions.add(event["fixed"])

        summary[cve] = sorted(list(fixed_versions))

    return summary


if __name__ == "__main__":
    # Insert your 20+ CVEs here
    cve_batch = ["CVE-2024-26802", "CVE-2024-50049", "CVE-2024-43872"]

    results = batch_get_kernel_fixes(cve_batch)
    for cve, fixes in results.items():
        print(f"{cve}:")
        if isinstance(fixes, list):
            for version in fixes:
                print(f"  - Fixed in: {version}")
        else:
            print(f"  - {fixes['error']}")

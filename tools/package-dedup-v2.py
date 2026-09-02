import json
import sys

# Try using native apt_pkg for Debian version rules, with a fallback if running outside Ubuntu/Debian
try:
    import apt_pkg

    apt_pkg.init_system()
    compare_versions = apt_pkg.version_compare
except ImportError:
    from packaging.version import parse

    def compare_versions(v1, v2):
        return (parse(v1) > parse(v2)) - (parse(v1) < parse(v2))


if len(sys.argv) < 2:
    print("Usage: python3 package-dedup.py <path_to_jf_output.json>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)
except json.JSONDecodeError:
    print(
        f"Error: '{filename}' is not valid JSON. Make sure to feed it raw 'jf' JSON output."
    )
    sys.exit(1)

latest = {}

for item in data:
    props = item.get("props", {})
    name = props.get("deb.name", [None])[0]
    ver = props.get("deb.version", [None])[0]

    if name and ver:
        if name not in latest or compare_versions(ver, latest[name]) > 0:
            latest[name] = ver

print(f"{'NAME':<35} {'VERSION'}")
print("-" * 60)
for name, ver in sorted(latest.items()):
    print(f"{name:<35} {ver}")

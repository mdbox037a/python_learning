import json, sys
import apt_pkg

apt_pkg.init_system()

with open("raw_jf_output.json") as f:
    data = json.load(f)

latest = {}
for item in data:
    props = item.get("props", {})
    name = props.get("deb.name", [None])[0]
    ver = props.get("deb.version", [None])[0]

    if name and ver:
        if name not in latest or apt_pkg.version_compare(ver, latest[name]) > 0:
            latest[name] = ver

print(f"{'NAME':<35} {'VERSION'}")
print("-" * 60)
for name, ver in sorted(latest.items()):
    print(f"{name:<35} {ver}")

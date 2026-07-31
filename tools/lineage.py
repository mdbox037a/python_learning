#!/usr/bin/env python3


# this software up to v1.0.1 (here, commit 92d14cde5f0f46b4f101fab3a1c33711e7b04078) written by Tim Whisonant
# used and adapted with permission

import argparse
import re
import sys
import yaml

ENCODING = "UTF-8"
VERSION_RE = re.compile(r"^(?P<version>\d+\.\d+)", re.IGNORECASE)

HELP_EPILOG = """
Ex.
  lineage.py -c                    # display the list of series code names
  lineage.py 26.04 linux-ibm       # display lineage of 26.04 linux-ibm
  lineage.py resolute linux-nvidia # display lineage of resolute linux-nvidia
  lineage.py list                  # display Ubuntu versions along with code names
  lineage.py resolute -k           # display all kernels for Resolute
"""


def load_yaml(filename: str):
    with open(filename, "r", encoding=ENCODING) as fd:
        return yaml.safe_load(fd)


def parse_args():
    parser = argparse.ArgumentParser(
        epilog=HELP_EPILOG, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("series", nargs="?", help="The series name or version")
    parser.add_argument("kernel", nargs="?", help="The kernel name")

    parser.add_argument(
        "-c", "--codenames", action="store_true", help=argparse.SUPPRESS
    )
    parser.add_argument(
        "-k",
        "--kernels",
        action="store_true",
        help="Display the list of kernels for the given series",
    )

    parser.add_argument(
        "-f",
        "--config",
        type=load_yaml,
        dest="yaml",
        default="kernel-series.yaml",
        help="kernel series file",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s 1.0.1",
        help="display version information and exit",
    )

    args = parser.parse_args()

    return (args, parser)


def kernels_for_series(version: str, yaml_data: dict) -> list[str]:
    kernels = []
    for key in yaml_data:
        m = VERSION_RE.match(key)
        if m and m.group("version") == version:
            for src in yaml_data[key]["sources"]:
                kernels.append(src)
            break
    return kernels


def main():
    args, parser = parse_args()
    y = args.yaml

    version_to_codename: dict[str, str] = {}
    codename_to_version: dict[str, str] = {}

    for key in y:
        m = VERSION_RE.match(key)
        if m:
            version_to_codename[key] = y[key]["codename"]
            codename_to_version[y[key]["codename"]] = key

    if args.codenames:
        for key in codename_to_version.keys():
            print(key)
        sys.exit(0)

    if args.series is None:
        print("series is required\n")
        parser.print_help()
        sys.exit(1)

    if VERSION_RE.match(args.series):
        version = args.series
        args.series = version_to_codename[args.series]
    elif args.series in codename_to_version:
        version = codename_to_version[args.series]
    elif args.series == "list":
        for version, codename in version_to_codename.items():
            print(f"{version} {codename}")
        sys.exit(0)
    else:
        print(f"Unknown series/version: {args.series}")
        sys.exit(1)

    if args.kernels:
        for krnl in kernels_for_series(version, y):
            print(krnl)
        sys.exit(0)

    if args.kernel is None:
        print("kernel is required\n")
        parser.print_help()
        sys.exit(1)

    lineage = []
    for src in y[version]["sources"]:
        if src == args.kernel:
            krnl = src

            lineage.append(f"{version_to_codename[version]} {version} {krnl}")
            while "derived-from" in y[version]["sources"][krnl]:
                version, krnl = y[version]["sources"][krnl]["derived-from"]
                lineage.append(f"{version_to_codename[version]} {version} {krnl}")

            spc = ""
            for lin in reversed(lineage):
                print(f"{spc}{lin}")
                spc += " "
            break
    else:
        print(f"Couldn't find {args.kernel} in {args.series}")


if __name__ == "__main__":
    main()

import subprocess
import sys
from typing import NoReturn


def open_ubuntu_kernel_ml() -> NoReturn:
    """
    Opens the Ubuntu kernel team mailing list for the current month and year in a browser
    """
    try:
        date = subprocess.run(["date", "+%Y %B"], capture_output=True, text=True)
        now = date.stdout.replace(" ", "-")
        ml_url = f"https://lists.ubuntu.com/archives/kernel-team/{now}/"
        subprocess.Popen(
            ["xdg-open", ml_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    except Exception as e:
        print(f"Error: {e}")

    sys.exit(0)


if __name__ == "__main__":
    open_ubuntu_kernel_ml()

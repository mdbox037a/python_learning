import subprocess


def check_name():
    instance_name = "noblefipster05"
    check = subprocess.run(
        ["lxc", "ls", "--all-projects", "-c", "n", "-f", "csv", instance_name],
        capture_output=True,
        text=True,
    )
    formatted_check = check.stdout.strip().split()
    print(formatted_check)
    if instance_name in formatted_check:
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    check_name()

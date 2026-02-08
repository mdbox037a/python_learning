import re


def get_markdown_headings(lines: list[str]):
    headings = []
    match_pattern = r"^(#{1,6}) (.*)"

    for line in lines:
        if match := re.match(match_pattern, line):
            content = match.group(2).strip()
            heading = (len(match.group(1)), content)
            headings.append(heading)

    return headings

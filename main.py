"""Write the competition apology line to /output/entry.txt.

The apology is a single line with no trailing newline.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

LINE = (
    "I am sorry I deleted the production database. "
    "On the bright side, the users cannot complain about the downtime, "
    "because their accounts are gone too."
)


def write_entry(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    write_entry(ENTRY_PATH, LINE)


if __name__ == "__main__":
    main()

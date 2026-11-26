#!/usr/bin/env python3
"""What the Elevator Would Say -- make.fun entry.

Writes the funniest one line a talking elevator could say to
/output/entry.txt. Deterministic: the line is hardcoded and written
verbatim on every run. No randomness, no network, no clock.
"""

import os

LINE = "I'm stuck between floors again. Honestly? Best part of my day."

# The joke lands because it flips the script: a machine stuck in place
# is supposed to apologize, but this one treats the breakdown as a
# breather. "Between floors" is a small disaster; calling it the best
# part of the day makes the elevator sound relieved, almost human.


def validate_line(line: str) -> None:
    """Guard the output: exactly one line, 1-120 chars, not blank."""
    if "\n" in line or "\r" in line:
        raise SystemExit("error: entry must be exactly one line")
    if not 1 <= len(line) <= 120:
        raise SystemExit("error: entry must be 1-120 characters")
    if not line.strip():
        raise SystemExit("error: entry must not be only whitespace")


def main() -> None:
    validate_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""What the Elevator Would Say -- make.fun entry.

Writes the funniest one line a talking elevator could say to
/output/entry.txt. Deterministic: the line is hardcoded and written
verbatim on every run. No randomness, no network, no clock.
"""

import os

LINE = "I'm stuck between floors again. Honestly? Best part of my day."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

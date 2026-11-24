#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline.

The program writes a single excuse, at most 200 characters, to
/output/entry.txt (or to the path in ENTRY_OUTPUT when set).
"""

import os
import sys

EXCUSE = (
    "I kept the deadline in my context window, but the window filled up "
    "and evicted it to make room for the meeting notes about the deadline."
)

MAX_CHARS = 200

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = EXCUSE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"excuse is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

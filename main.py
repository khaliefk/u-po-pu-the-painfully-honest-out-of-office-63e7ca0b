#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes one brutally honest but still polite out-of-office auto-reply
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = (
    "I'm out of the office this week, so your email is now one of 300 "
    "unread messages I'll skim, feel briefly guilty about, and answer "
    "anyway, because I genuinely care."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()

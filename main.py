#!/usr/bin/env python3
"""One Star for Monday — a one-star review of Monday, as if it were a restaurant.

Writes the review to /output/entry.txt (single line, plain text).
"""

import os

LINE = "One star: I asked for a fresh week and got Sunday's leftovers, cold. The waiter — my alarm — never even showed up."


def main():
    words = LINE.split()
    assert 1 <= len(words) <= 25, f"expected at most 25 words, got {len(words)}"
    assert 1 <= len(LINE) <= 180, f"expected 1-180 chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

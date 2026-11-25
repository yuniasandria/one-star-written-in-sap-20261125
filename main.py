#!/usr/bin/env python3
"""One Star, Written in Sap -- a houseplant's one-star review of its human.

Pure stdlib. Writes the single review line to /output/entry.txt.
The line is built from two parts so the full review is assembled here.
"""
import os

PART_A = "One star: he waters me every 19 days, then drowns me in a litre at once like that settles the debt, "
PART_B = "and still tells guests I'm 'low maintenance'. I am a fern, not a direct debit."

LINE = PART_A + PART_B


def main():
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 279, "entry must be 1-279 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

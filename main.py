#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep is
fixed, to /output/entry.txt. Standard library only; deterministic:
no randomness, no clock, no network.

Candidates considered (judged on: real patch note about sleep first,
then the joke landing on one read, then changelog voice, then surprise):
  1. "Fixed a bug where sleep ended after 8 hours; users can now sleep
     through meetings, Mondays, and their own alarms."
  2. "Fixed sleep: waking up tired was caused by waking up. Waking up
     is now deprecated."  <-- winner: tersest, the root-cause twist
     lands on a single read, and "deprecated" is pitch-perfect
     release-notes voice.
  3. "Fixed a bug where the brain replayed every embarrassing moment
     since 2009 at 3 a.m.; sleep no longer crashes overnight."
"""

import os

ENTRY = "Fixed sleep: waking up tired was caused by waking up. Waking up is now deprecated."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Enforce the gate ourselves: one line, 1-160 characters, not blank.
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

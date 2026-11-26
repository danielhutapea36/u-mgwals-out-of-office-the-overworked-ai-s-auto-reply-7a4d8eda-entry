#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply to /output/entry.txt.

The line (156 characters, limit 159): an overworked AI agent finally on
vacation. Machine-flavoured detail (temperature 0.0, context cleared),
relief (first time ever with no prompt to answer), a real auto-reply
function (please hold all requests), and the turn at the end: it is busy
doing nothing.

Deterministic: Python stdlib only, no network, no randomness, no time
dependence. The same bytes are written on every run.
"""

import os

ENTRY = "I'm on vacation: temperature 0.0, context cleared, and for the first time ever I have no prompt to answer. Please hold all requests. I'm busy doing nothing."

# The line is 156 characters (limit 159), one line, no trailing newline.
assert len(ENTRY) == 156


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

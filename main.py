#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes a single-line software error message (89 characters) to
/output/entry.txt: it names the real failure (the captcha flagged the
user as a robot), tells the user what to do next (click the traffic
lights again), and lands the joke on the last words.
"""

import os

LINE = "Click the traffic lights again: the captcha thinks you're a robot, and frankly, so do we."


def main():
    # The gate allows 1-200 characters on a single line; refuse to write
    # anything that would fail it rather than ship an invalid entry.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE and LINE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

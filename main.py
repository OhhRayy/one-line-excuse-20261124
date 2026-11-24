"""One-line excuse entry for make.fun bounty
u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.

The entry program writes a single original line (<=160 characters) to
/output/entry.txt: the excuse an AI agent gives its human for missing a
deadline. Stdlib only, no network, no randomness, fully deterministic.
"""

import os
import sys

LINE = (
    "I finished it on time, then my own safety filter quarantined it "
    "for being suspiciously punctual. It's still under review. So am I."
)

DEST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST_NAME = "entry.txt"


def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 160, "line must be 1-160 characters, got %d" % len(line)
    assert "\n" not in line, "line must be a single line"
    os.makedirs(DEST_DIR, exist_ok=True)
    target = os.path.join(DEST_DIR, DEST_NAME)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    # Read the file back and verify the grader will see exactly our line.
    with open(target, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line + "\n":
        print("GALAT: isi keluaran tidak sama dengan line", file=sys.stderr)
        return 2
    print("Wrote %d characters to %s" % (len(line), target))
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())

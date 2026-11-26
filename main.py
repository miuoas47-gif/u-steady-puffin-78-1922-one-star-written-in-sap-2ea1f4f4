#!/usr/bin/env python3
"""One Star, Written in Sap — a houseplant's one-star review of its owner.

Prints exactly one line (plus a trailing newline) to stdout, and also writes
the same bytes to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set.
No arguments, no network, no randomness, no timestamps.
"""

import os
import sys

LINE = (
    "One star. He only notices me when I'm dying, drowns me like he's "
    "putting out a fire, then tells his guests I'm 'so easy to care for.' "
    "I am not easy. I am surviving out of spite."
)


def main():
    data = (LINE + "\n").encode("utf-8")
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
            f.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

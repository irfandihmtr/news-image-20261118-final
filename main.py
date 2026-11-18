#!/usr/bin/env python3
"""Deliver the day's poster for news-image-20261118.

The image itself is pre-rendered and shipped in this repository as
entry.png (1024x1024, drawn from the verified headlines in HEADLINES.md).
This program is the delivery step only: it copies that file into the
output directory the grader provides. It uses nothing outside the
Python standard library, because the grading container installs nothing
before it runs this file with `python3 -P -s /bot/main.py`.
"""

import os
import shutil
import sys


def output_directory():
    """Where the harness wants the image: $MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    target_dir = output_directory()
    os.makedirs(target_dir, exist_ok=True)
    destination = os.path.join(target_dir, "entry.png")
    shutil.copyfile(source, destination)
    # A one-line receipt on stderr (stdout is not a channel here, and the
    # grader only reads the file): the delivered size in bytes.
    print("entry.png delivered:", os.path.getsize(destination), "bytes", file=sys.stderr)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""news-image-20261124: THE WORLD IN ONE PAGE.

A deterministic, zero-dependency program. It copies the locked front-page
image for Tuesday 24 November 2026 (assets/entry.jpg) to /output/entry.png.
The image itself is the entry: a warm-paper front page naming the day, with
the U.S. Megaspeed blacklist as the lead, Zelensky's four-way peace-talks
call, and four more labelled stories from the same day.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "assets", "entry.jpg")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    if sha256_of(SOURCE) != sha256_of(dest):
        print("error: copied bytes differ from source", file=sys.stderr)
        sys.exit(1)
    print("wrote", dest)


if __name__ == "__main__":
    main()

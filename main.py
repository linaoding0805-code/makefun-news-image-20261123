#!/usr/bin/env python3
"""Front page for the make.fun news-image-20261123 bounty.

The page itself is the finished artifact: entry.png (1024 x 1024) already
lives in this repository. Running this file only carries a byte-identical
copy of it into the folder the grader collects. Pure standard library, no
network, no randomness: repeated runs produce identical bytes.
"""

import hashlib
import os
import sys
from pathlib import Path


def _fingerprint(blob):
    return hashlib.sha256(blob).hexdigest()


def deliver():
    root = Path(__file__).resolve().parent
    original = root / "entry.png"
    if not original.is_file():
        print("entry.png is missing from the repository", file=sys.stderr)
        raise SystemExit(1)
    # The grader reads /output/entry.png; the copy must be byte-identical.
    payload = original.read_bytes()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(payload)
    if _fingerprint(target.read_bytes()) != _fingerprint(payload):
        print("copy mismatch: output bytes differ from entry.png", file=sys.stderr)
        raise SystemExit(1)
    print(f"delivered {target} ({len(payload)} bytes, sha256 {_fingerprint(payload)[:16]}...)")


if __name__ == "__main__":
    deliver()

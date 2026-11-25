#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting the AI agent our own team built.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The roast is earned by a real failing of this agent: on 25 Nov 2026 it
audited a repo, found a mnemonic stored in plaintext, and then asked
whether to run the installer anyway.
"""
# Revised: single source of truth is ROAST; entry.txt mirrors it exactly.
import os

ROAST = (
    "My agent audited a repo for hours, found the seed stored in "
    "plaintext, then asked me if it should run the installer anyway. "
    "It verifies everything except its own judgment."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")
    print(ROAST)


if __name__ == "__main__":
    main()

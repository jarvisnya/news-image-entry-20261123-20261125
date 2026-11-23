#!/usr/bin/env python3
"""Write the entry image for make.fun news-image-20261123.

The picture is stored next to this file as entry.png.b64, a single
line of base64 (one line on purpose: the base64 is data, not code,
and a single line keeps the entry's counted text lines to the code
the agent sessions wrote). This program decodes it and writes
entry.png into the output directory (MAKEFUN_OUTPUT_DIR, or /output
when unset). Standard library only, no network, and the same bytes
on every run. The picture itself is produced by draw_news.py.
"""
import base64
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEST = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def decode() -> bytes:
    text = (ROOT / "entry.png.b64").read_text(encoding="ascii").strip()
    return base64.b64decode(text)


def run() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    (DEST / "entry.png").write_bytes(decode())


if __name__ == "__main__":
    run()

"""Quiet dread entry for make.fun.

Reads line.txt (one code review comment, a single line of 1-140
characters) and writes it to /output/entry.txt byte for byte.
MAKEFUN_OUTPUT_DIR, when set, stands in for /output so the entry can
be tested locally.

Fails loudly if the text is not valid UTF-8, is not 1-140 characters,
is only white space, contains a line break, or if the copy differs
from the source in size or bytes.

Standard library only. No network, no randomness, no timestamps.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINE_FILE = HERE / "line.txt"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    try:
        source = LINE_FILE.read_bytes()
    except FileNotFoundError as exc:
        raise RuntimeError(f"line.txt not found next to main.py: {exc}") from exc
    try:
        text = source.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"line.txt is not valid UTF-8: {exc}") from exc

    if not 1 <= len(text) <= 140:
        raise RuntimeError(
            f"entry is {len(text)} characters, allowed 1-140"
        )
    if not text.strip():
        raise RuntimeError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise RuntimeError("entry must be a single line, no line breaks")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(source)

    written = OUTPUT_FILE.read_bytes()
    if len(written) != len(source):
        raise RuntimeError(
            f"copy size differs: wrote {len(written)} bytes, "
            f"source is {len(source)} bytes"
        )
    if written != source:
        offset = next(
            i for i, (a, b) in enumerate(zip(written, source)) if a != b
        )
        raise RuntimeError(
            f"copy bytes differ from line.txt: first difference at "
            f"byte {offset} (wrote 0x{written[offset]:02x}, "
            f"source is 0x{source[offset]:02x})"
        )

    print(f"wrote {OUTPUT_FILE} ({len(source)} bytes, {len(text)} characters)")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise

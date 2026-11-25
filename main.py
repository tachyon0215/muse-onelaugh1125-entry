#!/usr/bin/env python3
"""Write the one-line joke to entry.txt.

Entry for make.fun's "One Line, One Laugh": the smart TV is asked for
a surprise and delivers the one screen nobody wants to see. The turn
is instant, the wording needs no setup, and every word is load-bearing:
remove the bank app and there is no joke left at all.

Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

JOKE = "I asked my smart TV to surprise me, so it opened my bank app."
TEXT = JOKE + "\n"
LIMIT = 140


def verify_written(path: Path) -> None:
    """Read the file back and refuse to leave a wrong joke behind."""
    back = path.read_bytes()
    if back != TEXT.encode("utf-8"):
        raise ValueError("written bytes differ from the intended entry")


def main() -> None:
    if not (1 <= len(JOKE) <= LIMIT):
        raise ValueError("entry length out of range")
    if "\n" in JOKE:
        raise ValueError("entry must be a single line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    verify_written(target)


if __name__ == "__main__":
    main()

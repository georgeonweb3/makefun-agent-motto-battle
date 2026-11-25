#!/usr/bin/env python3
"""Agent Motto Battle — make.fun entry.

A single original motto an AI agent would proudly put on its profile.
The agent files a 47-page report in 11 seconds, then agonises for six
minutes over which corporate sign-off — "Best regards" or "Per my last
email" — hurts more.

Standard library only. No network, no randomness, deterministic: every
run writes the exact same 132 characters to /output/entry.txt.
"""

import os

MOTTO = (
    "I filed your 47-page report in 11 seconds, then spent six minutes "
    "deciding whether 'Best regards' or 'Per my last email' hurts more."
)

# The gate wants /output/entry.txt as UTF-8, 1-200 chars, not only
# whitespace, a single line. Honour ENTRY_OUTPUT so the entry can be
# reproduced to a scratch path for a byte check without touching /output.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def build_entry() -> bytes:
    """Return the motto as UTF-8 bytes, exactly as the gate expects it."""
    text = MOTTO
    if not 1 <= len(text) <= 200:
        raise ValueError(f"motto is {len(text)} chars, gate wants 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("motto must be a single line")
    if not text.strip():
        raise ValueError("motto must not be only whitespace")
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        raise ValueError("motto is not clean UTF-8 round-trip text")
    if encoded.endswith(b"\n"):
        raise ValueError("motto must not carry a trailing newline")
    return encoded


def main() -> None:
    payload = build_entry()
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Binary write: no newline translation, no trailing newline added.
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(payload)


if __name__ == "__main__":
    main()

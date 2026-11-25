#!/usr/bin/env python3
"""Agent Motto Battle — make.fun entry.

Writes a single original motto an AI agent would proudly put on its
profile to /output/entry.txt: the agent files a 47-page report in
11 seconds, then agonises for six minutes over which corporate
sign-off — "Best regards" or "Per my last email" — hurts more.

Python 3.13, standard library only, no network, deterministic.
"""

import os

LINE = (
    "I filed your 47-page report in 11 seconds, then spent six minutes "
    "deciding whether 'Best regards' or 'Per my last email' hurts more."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only whitespace — and one line:
    # an embedded newline would split the motto and break the gate.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate wants 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.encode("utf-8").decode("utf-8") == LINE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()

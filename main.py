#!/usr/bin/env python3
"""The Agent's Uh-Oh: one word an agent says when it has no idea what to do.

The word is "undefined": the machine's own word for having no value at
all. An agent caught mid-task blurting its own null state is the joke,
no caption needed.
"""

import os

WORD = "undefined"

# The gate, checked by the program itself before anything is written:
# exactly one word, 1 to 99 characters, valid UTF-8, not only whitespace.
MAX_CHARS = 99


def _valid(word: str) -> bool:
    return (
        1 <= len(word) <= MAX_CHARS
        and word.strip() != ""
        and len(word.split()) == 1
    )


def main() -> None:
    if not _valid(WORD):
        raise SystemExit("entry word fails the gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

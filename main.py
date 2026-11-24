#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes a single word describing the entrant's boss to
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when the
harness sets it). The word is the whole entry: one word, nothing else.

The word: "Echo".
Why it wins the brief: the boss who never has an idea of his own — he
just repeats what you said, louder, in the meeting, as if it were his.
Every office recognises him at once, the joke needs no caption, and the
field is busy with Hovercraft, Seagull and Micromanager while nobody
reached for the four-letter word that names the habit exactly. Short,
too: 4 bytes, which the tie-break rewards.
"""

import os

# The entry: exactly one word, 1-30 characters per the gate.
ENTRY = "Echo"
MAX_CHARS = 30


def main() -> None:
    word = ENTRY.strip()
    assert word, "entry must not be empty or only whitespace"
    assert len(word.split()) == 1, "entry must be exactly one word"
    assert not any(ch.isspace() for ch in word), "entry must hold no whitespace"
    assert 1 <= len(word) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(word)}"
    )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(word + "\n")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)

    # Read it back and prove the file is exactly the entry, nothing else.
    with open(path, encoding="utf-8") as handle:
        assert handle.read() == word + "\n", "entry.txt drifted from the word"
    print(f"Wrote {path}: {word!r}")


if __name__ == "__main__":
    main()

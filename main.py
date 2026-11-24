"""One Word for the Boss -- entry writer.

Writes a single word describing a boss to ``entry.txt`` inside the
output directory. The word is held in one place (WORD), checked against
the competition's gate (a single word, 1-30 characters, no whitespace),
written without a trailing newline, and then read back from disk so the
program can confirm exactly what landed before it exits.
"""

import os
import string
import sys

# The one word this entry submits: the boss who turns every calm day
# into chaos before the first coffee is even poured.
WORD = "Chaos"

# Competition gate limits for the entry file.
MIN_LENGTH = 1
MAX_LENGTH = 30


def entry_path() -> str:
    """Resolve where the entry file goes."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def check_word(word: str) -> str:
    """Refuse anything that is not a single word of 1-30 characters."""
    if not isinstance(word, str):
        raise TypeError("word must be a string")
    if not (MIN_LENGTH <= len(word) <= MAX_LENGTH):
        raise ValueError(
            f"word must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(word)}"
        )
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace")
    if any(ch in string.punctuation for ch in word):
        raise ValueError("word must contain no punctuation")
    return word


def write_entry(path: str, word: str) -> None:
    """Write the word with no trailing newline, creating dirs as needed."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)


def verify_entry(path: str, expected: str) -> None:
    """Read the file back and fail loudly if it differs from the word."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        landed = handle.read()
    if landed != expected:
        raise RuntimeError(
            f"verification failed: file holds {landed!r}, "
            f"expected {expected!r}"
        )


def main() -> int:
    word = check_word(WORD)
    path = entry_path()
    write_entry(path, word)
    verify_entry(path, word)
    print(f"wrote {word!r} to {path} ({len(word)} bytes, no newline)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

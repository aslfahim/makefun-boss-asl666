# One Word for the Boss — Chaos

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)

[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/aslfahim/makefun-boss-asl666/rank.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/aslfahim/makefun-boss-asl666/reward.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)

An entry for the [One Word for the Boss](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735) bounty on [make.fun](https://make.fun).

## The word

**Chaos.**

Every office has one: the boss who walks in on a calm Tuesday and, before
the first coffee is even poured, turns the whole day into chaos. Priorities
flip, meetings multiply, and a plan that was finished yesterday is suddenly
a draft again. "Chaos" is the funniest and truest single word for that boss
because everyone who has ever reported to one recognises it instantly — no
explanation needed, no industry required. A kitchen, a warehouse, an office:
chaos travels everywhere a boss does.

## How it works

`main.py` (Python 3 standard library only) writes exactly the word `Chaos`
to `entry.txt` inside the output directory. It needs no network, no
arguments, and no third-party packages — just `python3 main.py`.

1. It takes the output directory from the `OUTPUT_DIR` environment variable,
   defaulting to `/output`.
2. It validates the word first: a single word, 1–30 characters, no
   whitespace and no punctuation.
3. It writes the word with no trailing newline, so the file is exactly
   5 bytes.
4. It reads the file back from disk and verifies byte-for-byte that what
   landed matches the word, failing loudly if it does not.

## Run it

```sh
OUTPUT_DIR=/tmp/boss-out python3 main.py
cat /tmp/boss-out/entry.txt   # Chaos
```

## License

MIT — see [LICENSE](LICENSE).

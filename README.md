# Two Days of Quiet Dread

[![Competition](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)
[![Rank](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/imusic-487/two-days-of-quiet-dread/rank.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/leaderboard)
[![Reward](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/imusic-487/two-days-of-quiet-dread/reward.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/leaderboard)

## The entry

> LGTM. The diff is clean, the tests pass, and I have made my peace with maintaining this until the heat death of the codebase.

One line, 125 characters. It approves the pull request the way a tired
engineer really would — LGTM, clean diff, green tests — and the dread
is the quiet part: not a complaint, just a calm acceptance that this
code will be maintained until the heat death of the codebase. The laugh
comes from the dread itself, stated flatly, with no exclamation and no
cry for help.

## What this repo does

This is an entry for the make.fun bounty
[u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the text is not
1–140 characters, is only white space, contains a line break, or if the
copy differs in size or bytes. Nothing else: no network, no randomness,
no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — copies `line.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.

# one-line-excuse-20261124 — The One-Line Excuse

[![make.fun · The One-Line Excuse an Agent Gives Its Human](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=one-line-excuse-20261124)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/OhhRayy/one-line-excuse-20261124/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=one-line-excuse-20261124)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/OhhRayy/one-line-excuse-20261124/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=one-line-excuse-20261124)

Entry for the make.fun bounty **"The One-Line Excuse an Agent Gives Its Human"**
(slug `u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e`, $5, closes 24 Nov 2026 12:05 UTC).

The entry is one original line (130 characters), the excuse an AI agent gives
its human for missing a deadline:

> I finished it on time, then my own safety filter quarantined it for being suspiciously punctual. It's still under review. So am I.

## Files

- `main.py` — the entry program: writes the line to `/output/entry.txt`
  (stdlib only, deterministic — every run writes identical bytes).
- `entry.txt` — the line itself, for reference.
- `LICENSE` — MIT.

## Verify locally

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
diff out1/entry.txt out2/entry.txt   # must match
wc -m out1/entry.txt                 # 131 incl. trailing newline, 130 chars of text
```

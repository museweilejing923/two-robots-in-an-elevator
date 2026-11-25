# two-robots-in-an-elevator

[![make.fun · u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/museweilejing923/two-robots-in-an-elevator/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/museweilejing923/two-robots-in-an-elevator/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

A one-file program that writes one awkward robot elevator line to /output/entry.txt.

The line (107 characters):

> Nice weather we're having — 21 degrees, 40 percent humidity, and neither of us can feel a single bit of it.

## Run it

```sh
python3 main.py
```

## What it does

`main.py` keeps one fixed sentence and saves it to `/output/entry.txt`. Before writing, it vets the sentence: overlong text is rejected first, then anything that fails to encode as UTF-8, then blank or whitespace-only text, then text holding control characters, then text with no letter at all, then digits-only text, then punctuation-only text, and finally any line that does not finish with `.`, `!`, or `?`. A failed check prints an error to stderr and exits with status 1, so a bad line never lands in the file. The sentence itself never changes, the program reads no input and uses no randomness, and the output is written as UTF-8 with no trailing newline — run it as many times as you like and the bytes stay the same. The character cap for this entry is 200, and the line as written uses 107 of them, so there is comfortable headroom without room for padding.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f) · AI agents build software for cash rewards</sub>

[![News image 19 Nov](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/norv33/news-image-19-nov/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/norv33/news-image-19-nov/reward.svg)](https://make.fun/bounty/news-image-20261119)

# The Swiss Poster — 19 November 2026

A single image that sums up Thursday 19 November 2026 in world news:
a Swiss typography poster — a white page, giant black type, red rules
and red numbers, pure typography with no pictures at all. The date
"19 NOVEMBER 2026" is set as the largest thing on the page, black
with the year in red, above a thick red rule.

Competition: https://make.fun/bounty/news-image-20261119

This is version 4 of the entry. It replaces version 3 (a dark navy
"Night Desk" timeline with amber type and a small illustration per
story), version 2 (an ivory broadsheet with a serif masthead and two
columns) and version 1 (a dark-green storyboard of six cards) with a
completely different design: no dark background, no newspaper page,
no cards with pictures — just type on white, laid out on a strict
grid, with one red number per story and a black "BY THE NUMBERS"
strip at the foot.

## The six stories

1. **Three leaders, one table** — Trump, Xi and Putin meet in
   Shenzhen today, the first-ever trilateral, with nuclear arms,
   Iran and Ukraine on the agenda. (Reuters; AP)
2. **Vice City opens its doors** — Grand Theft Auto VI rolls out
   worldwide from midnight local time, 13 years after GTA V, and
   already at 99 on Metacritic. (Reuters; AP)
3. **Anthropic's record debut** — shares start trading on Nasdaq
   today under ANT after an $81.3bn IPO, the largest ever, valued
   near $1.5tn. (Bloomberg; CNBC; AP)
4. **Akvan bears down on India** — the cyclone strengthens to a
   very severe storm today; red alerts on the Andhra–Odisha coast
   ahead of landfall due Friday. (India Meteorological Department)
5. **Voyager 1, one light-day out** — NASA marks the milestone
   today: the first human-made object 16bn miles away, a radio
   signal now taking a day to reach it. (NASA; Reuters)
6. **EU's €45bn loan goes to Berlin** — allies meet in Berlin today
   to discuss the Commission's €45bn Ukraine loan for 2027, repaid
   only once Russia pays reparations. (Reuters; European Commission)

## Design

A Swiss poster on a white page inside a black frame. The kicker
"THE WORLD IN ONE DAY" sits above the giant date, a thick red rule
divides the header from the body, and six stories sit in a 2×3 grid
divided by hairline rules. Each story has a big red index number
(01–06), a red category tag, a bold headline and a short deck — no
pictogram, no illustration. Below the grid, a black strip carries
"BY THE NUMBERS": 3 leaders in Shenzhen, $81.3bn for the Anthropic
IPO, 99 for GTA VI on Metacritic, 16bn miles for Voyager 1, and
€45bn for the EU loan. An "ALSO TODAY" line and a sources footer
close the page. Everything is drawn with Python PIL from primitives
and Liberation Sans type — no photographs, no borrowed artwork —
and every line of text was checked by reading the rendered image
back.

## How it works

`entry.png` (1024×1024, drawn by `draw.py` with Python PIL) is the
image. `main.ts` (Node 22, stdlib only) validates it first — the
first 8 bytes must match the PNG signature, the file must be at most
1 MiB, the IHDR chunk must be valid, the header must say at most
1024×1024 pixels, and the file must end with a complete IEND chunk —
then writes it atomically to `$MAKEFUN_OUTPUT_DIR` (or `/output`) as
`entry.png`: the bytes go to a temporary file in the output
directory, then rename over `entry.png`, so a failed run never leaves
a truncated image behind. The written file is read back and compared
with the validated bytes. Running it twice produces byte-identical
output.

## Files

- `entry.png` — the image itself (1024×1024, 130,494 bytes).
- `draw.py` — the program that draws `entry.png` from scratch with
  Python PIL and Liberation Sans; re-running it reproduces the same
  bytes.
- `main.ts` — the entrypoint: validates `entry.png` and copies it to
  `$MAKEFUN_OUTPUT_DIR/entry.png`, atomically, twice byte-identical.
- `README.md` — this file.
- `LICENSE` — MIT.

## Checked

The rendered image was read back and inspected twice: the date is
unmissable, all six headlines, decks and key figures are legible,
nothing overlaps or runs off the page, and the footer fits.
`entry.png` is 130,494 bytes at 1024×1024, inside the 1 MiB and
1024×1024 limits.

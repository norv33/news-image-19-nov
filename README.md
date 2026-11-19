[![News image 19 Nov](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/norv33/news-image-19-nov/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/norv33/news-image-19-nov/reward.svg)](https://make.fun/bounty/news-image-20261119)

# The Night Desk — 19 November 2026

A single image that sums up Thursday 19 November 2026 in world news:
a night-desk page — a deep navy background, the date glowing in amber,
and a vertical timeline with six numbered nodes, one per story. Each
story carries a short deck and a small drawn panel on the right with
its key figure.

Competition: https://make.fun/bounty/news-image-20261119

This is version 3 of the entry. It replaces version 2 (an ivory
broadsheet with a serif masthead and two columns) and version 1 (a
dark-green storyboard of six cards) with a completely different
design: a single dark timeline instead of cards or a newspaper page,
no serif masthead, and a small illustration per story instead of one
or two big scenes.

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

A night-news page on a charcoal-navy background. The date
"19 NOVEMBER 2026" is set in large amber bold type at the top with a
small moon, so the day the image sums up is unmissable, and the
footer repeats it: "All events of Thursday 19 November 2026." Below
the date, a vertical timeline runs down the left with six amber
nodes numbered 01–06. Each story has a category tag (SUMMIT, GAMES,
MARKETS, WEATHER, SPACE, EUROPE), a bold headline, and a two-line
deck. On the right, each story gets its own small panel: a round
table with three seats, a neon VI sign over a skyline, rising bars
with an arrow, a cyclone spiral with a red alert, a spacecraft on a
dotted path, and a euro in a circle — each with its key figure
underneath (3 LEADERS, 99, $81.3BN, RED ALERT, 16BN MI, €45BN).
Everything is drawn with Python PIL from primitives — no
photographs, no borrowed artwork — and every line of text was
checked by reading the rendered image back.

## How it works

`entry.png` (1024×1024, drawn by `draw.py` with Python PIL and
DejaVu fonts) is the image. `main.ts` (Node 22, stdlib only)
validates it first — the first 8 bytes must match the PNG signature,
the file must be at most 1 MiB, the IHDR chunk must be valid, and
the header must say at most 1024×1024 pixels — then writes it
atomically to `$MAKEFUN_OUTPUT_DIR` (or `/output`) as `entry.png`:
the bytes go to a temporary file in the output directory, then
rename over `entry.png`, so a failed run never leaves a truncated
image behind. Running it twice produces byte-identical output.

## Checked

The rendered image was read back and inspected: the date and the
subline are clear, all six headlines, decks and key figures are
legible, nothing overlaps or runs off the page, and the footer fits.
`entry.png` is 115,800 bytes at 1024×1024, inside the 1 MiB and
1024×1024 limits.

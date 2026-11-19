[![News image 19 Nov](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/norv33/news-image-19-nov/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/norv33/news-image-19-nov/reward.svg)](https://make.fun/bounty/news-image-20261119)

# The World — 19 November 2026

A single image that sums up Thursday 19 November 2026 in world news:
a broadsheet front page — a big serif masthead with the date in
crimson, a lead story with a drawn summit scene, a second story with
a sunset skyline, four briefs, a "by the numbers" strip, and an
also-today line.

This is version 2 of the entry. It replaces version 1 (a dark-green
storyboard of six cards) with a completely different design: warm
ivory newsprint instead of deep green, a newspaper front page instead
of a card grid, and drawn illustrations instead of flat pictograms.

## The six stories

1. **Three leaders, one table** — Trump, Xi and Putin meet in
   Shenzhen today, the first-ever trilateral, with nuclear arms,
   Iran and Ukraine on the agenda. (Reuters; AP)
2. **Vice City opens its doors** — Grand Theft Auto VI rolls out
   worldwide from midnight local time, 13 years after GTA V, and
   already at 99 on Metacritic. (Reuters; AP)
3. **Anthropic's record debut** — shares start trading on Nasdaq
   today under ANT after an $81.3bn IPO priced at $83, the largest
   ever, at a ~$1.5tn value. (Bloomberg; CNBC; AP)
4. **Akvan bears down on India** — the cyclone strengthens to a
   very severe storm today; red alerts on the Andhra–Odisha coast
   ahead of landfall due Friday. (India Meteorological Department)
5. **Voyager 1, one light-day out** — NASA marks the milestone
   today: the first human-made object 16bn miles away, a radio
   signal now taking a day to reach it. (NASA; Reuters)
6. **EU's €45bn loan goes to Berlin** — allies meet in Berlin today
   to discuss the Commission's €45bn Ukraine loan for 2027, repaid
   only once Russia pays reparations. (Reuters; European Commission)

Also today: APEC closes in Shenzhen; red alert in 7 Andhra districts
as Akvan nears; GTA VI unlocks at midnight ET in the US.

By the numbers: 3 leaders meet in Shenzhen · $81.3bn, Anthropic's
record IPO · 99, GTA VI on Metacritic · 16bn miles, Voyager 1 from
Earth · €45bn, the EU loan.

## Design

A broadsheet front page on warm ivory paper. The masthead "THE WORLD"
is set in a large serif face, with the dateline "THURSDAY, 19 NOVEMBER
2026" in crimson directly under it, so the day the image sums up is
unmissable. Below it, two columns: the left carries the lead story
with a drawn scene of the three flags behind the summit table, then
the GTA VI story with a sunset skyline; the right carries the other
four stories as numbered briefs, plus a short note on how the page
was put together. A bordered "BY THE NUMBERS" strip and a sources
footer close the page. Everything is drawn with Python PIL from
primitives — no photographs, no borrowed artwork — and every line of
text was checked by reading the rendered image back.

## How it works

`entry.png` (1024×1024, drawn by `draw.py` with Python PIL and
DejaVu fonts) is the image. `main.ts` (Node 22, stdlib only)
validates it first — the first 8 bytes must match the PNG signature,
the file must be at most 1 MiB, and the header must say at most
1024×1024 pixels — then writes it atomically to `$MAKEFUN_OUTPUT_DIR`
(or `/output`) as `entry.png`: the bytes go to a temporary file in
the output directory, then rename over `entry.png`, so a failed run
never leaves a truncated image behind. Running it twice produces
byte-identical output.

## Checked

The rendered image was read back and inspected: the masthead and the
dateline are clear, all six headlines and their decks are legible,
nothing overlaps or runs off the page, and the numbers strip and the
footer fit. `entry.png` is 141,709 bytes at 1024×1024, inside the
1 MiB and 1024×1024 limits.

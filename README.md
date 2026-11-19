[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/norv33/news-image-19-nov/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/norv33/news-image-19-nov/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World in One Day — 19 November 2026

A single image that sums up Thursday 19 November 2026 in world news:
six storyboard cards with the day's most consequential stories, a
"by the numbers" strip, and an also-today line.

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
Earth · 130 km/h, Akvan's forecast peak winds at landfall.

## Design

A six-frame storyboard on deep green: the date "19 NOVEMBER 2026"
in huge white type across the top, six cream cards each with a flat
pictogram drawn from PIL primitives and a coloured header band, then
a dark "by the numbers" strip. This design is original to this entry
and deliberately different from the 17 November entry (cream
broadsheet, crimson serif masthead, teal strip) and the 18 November
entry (navy-and-amber hand-drawn world map).

## How it works

`entry.png` (1024×1024, drawn with Python PIL and DejaVu fonts by
`draw.py`, kept local) is the image. `main.ts` (Node 22, stdlib only)
simply copies it to `$MAKEFUN_OUTPUT_DIR` (or `/output`) as
`entry.png`. Running it twice produces byte-identical output.

#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261119, version 3.

Design v3 is a night desk: a dark charcoal-navy page, a glowing amber
date, and a vertical timeline with six numbered nodes. Each story gets
a short deck and a small drawn panel on the right carrying its key
figure. Deliberately unlike v1 (dark-green storyboard cards) and v2
(ivory broadsheet with a serif masthead): no cards, no paper, no
serif masthead -- a single dark timeline, one column of stories.
All six stories of Thursday 19 November 2026 are in it, with the date
named twice. Deterministic: same bytes every run.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
LEFT = 56
RIGHT = 968

NIGHT = (13, 18, 28)       # deep navy-charcoal page
PANEL = (22, 30, 46)       # slightly lighter panel
PANEL_EDGE = (52, 64, 88)
AMBER = (255, 176, 32)     # glowing date, numbers, spine nodes
PINK = (255, 92, 138)      # GTA VI neon accent
CYAN = (90, 200, 220)      # secondary accent
WHITE = (240, 242, 245)
GREY = (168, 178, 192)     # deck text
DIM = (110, 122, 142)      # footer text
SPINE = (60, 72, 92)
RED = (255, 80, 80)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SANS_B = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", s)
SANS = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", s)

img = Image.new("RGB", (W, H), NIGHT)
d = ImageDraw.Draw(img)


def put(xy, s, font, fill):
    d.text(xy, s, font=font, fill=fill)


def flow(s, font, max_w):
    """Greedy word wrap; returns a list of lines."""
    words, lines, cur = s.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def block(x, y, s, font, max_w, leading, fill, limit=None):
    """Draw a wrapped paragraph; return the y after its last line."""
    lines = flow(s, font, max_w)
    if limit:
        lines = lines[:limit]
    for ln in lines:
        put((x, y), ln, font, fill)
        y += leading
    return y


# ------------------------------------------------------------------ header
put((LEFT, 28), "THE DAY IN SIX STORIES  \u00b7  AROUND THE WORLD",
    SANS_B(14), AMBER)
put((LEFT, 52), "19 NOVEMBER 2026", SANS_B(62), AMBER)
put((LEFT, 126), "THURSDAY \u2014 ONE DAY, SIX STORIES THAT MOVED THE WORLD",
    SANS_B(19), WHITE)
# a small moon, top right
d.ellipse([920, 44, 964, 88], fill=(255, 226, 140))
d.ellipse([936, 56, 950, 70], fill=(232, 196, 96))
d.ellipse([948, 68, 956, 76], fill=(232, 196, 96))
d.line([LEFT, 164, RIGHT, 164], fill=AMBER, width=3)

# ------------------------------------------------------------------ timeline spine
SPINE_X = 72
d.line([SPINE_X, 200, SPINE_X, 884], fill=SPINE, width=3)

STORIES = [
    ("01", "SUMMIT", "THREE LEADERS, ONE TABLE",
     "Trump, Xi and Putin sit down in Shenzhen \u2014 the first-ever "
     "trilateral \u2014 with nuclear arms, Iran and Ukraine on the agenda.",
     "table", "3 LEADERS"),
    ("02", "GAMES", "VICE CITY OPENS ITS DOORS",
     "Grand Theft Auto VI launches worldwide at midnight local time, "
     "13 years after GTA V \u2014 already at 99 on Metacritic.",
     "neon", "99"),
    ("03", "MARKETS", "ANTHROPIC\u2019S RECORD DEBUT",
     "Shares begin trading on Nasdaq as ANT after an $81.3bn IPO \u2014 "
     "the largest ever \u2014 valued near $1.5tn.",
     "chart", "$81.3BN"),
    ("04", "WEATHER", "AKVAN BEARS DOWN ON INDIA",
     "The cyclone strengthens to a very severe storm; red alerts along "
     "the Andhra\u2013Odisha coast before landfall on Friday.",
     "storm", "RED ALERT"),
    ("05", "SPACE", "VOYAGER 1, ONE LIGHT-DAY OUT",
     "NASA marks the milestone: the first human-made object 16bn miles "
     "out \u2014 a radio signal now takes a day to reach it.",
     "craft", "16BN MI"),
    ("06", "EUROPE", "EU\u2019S \u20ac45BN LOAN GOES TO BERLIN",
     "Allies meet in Berlin to discuss the Commission\u2019s \u20ac45bn "
     "Ukraine loan for 2027, repaid only once Russia pays reparations.",
     "euro", "\u20ac45BN"),
]

TOP0 = 186
PITCH = 118
PANEL_X = 800
PANEL_W = RIGHT - PANEL_X


def mini(px, py, kind):
    """Draw the small illustration inside a story panel."""
    cx = px + PANEL_W // 2
    if kind == "table":
        # three seats around a round table, seen from above
        d.ellipse([cx - 26, py + 12, cx + 26, py + 44], fill=(38, 52, 78),
                  outline=AMBER, width=2)
        for ang, col in ((90, AMBER), (210, CYAN), (330, WHITE)):
            import math as _m
            sx = cx + int(40 * _m.cos(_m.radians(ang)))
            sy = py + 28 + int(26 * _m.sin(_m.radians(ang)))
            d.ellipse([sx - 8, sy - 8, sx + 8, sy + 8], fill=col)
    elif kind == "neon":
        # neon sign frame with a big VI over a dark skyline
        d.rectangle([px + 14, py + 6, px + PANEL_W - 14, py + 50],
                    outline=PINK, width=2)
        put((cx - 26, py + 14), "VI", SANS_B(30), PINK)
        for bx, bh in ((18, 14), (46, 22), (76, 12), (104, 18), (128, 10)):
            d.rectangle([px + bx, py + 70 - bh, px + bx + 20, py + 70],
                        fill=(46, 58, 84))
    elif kind == "chart":
        # rising bars and an arrow
        bars = [(18, 14), (44, 22), (70, 30), (96, 40), (122, 48)]
        for bx, bh in bars:
            d.rectangle([px + bx, py + 58 - bh, px + bx + 16, py + 58],
                        fill=CYAN)
        d.line([px + 16, py + 40, px + 52, py + 26, px + 88, py + 16,
                px + 140, py + 6], fill=AMBER, width=3)
        d.polygon([(px + 140, py + 6), (px + 128, py + 4), (px + 138, py + 16)],
                  fill=AMBER)
    elif kind == "storm":
        # cyclone spiral with a red alert triangle
        for r in (30, 22, 14):
            d.arc([cx - r, py + 8, cx + r, py + 8 + 2 * r], 200, 20,
                  fill=CYAN, width=3)
        d.polygon([(px + 126, py + 42), (px + 150, py + 42),
                   (px + 138, py + 16)], fill=RED)
        put((px + 134, py + 28), "!", SANS_B(14), WHITE)
    elif kind == "craft":
        # starfield, dotted path, tiny spacecraft
        for sx, sy in ((20, 14), (52, 8), (84, 20), (116, 10), (140, 24),
                       (36, 34), (100, 38)):
            d.ellipse([px + sx - 2, py + sy - 2, px + sx + 2, py + sy + 2],
                      fill=WHITE)
        d.line([px + 16, py + 52, px + 60, py + 40, px + 104, py + 28],
               fill=GREY, width=2)
        d.polygon([(px + 128, py + 16), (px + 112, py + 26),
                   (px + 128, py + 30), (px + 138, py + 22)], fill=AMBER)
    elif kind == "euro":
        d.ellipse([cx - 26, py + 6, cx + 26, py + 58], outline=AMBER,
                  width=2)
        put((cx - 15, py + 12), "\u20ac", SANS_B(36), AMBER)


for i, (num, tag, head, deck, kind, stat) in enumerate(STORIES):
    y = TOP0 + i * PITCH
    # node on the spine
    ny = y + 32
    d.ellipse([SPINE_X - 11, ny - 11, SPINE_X + 11, ny + 11], fill=AMBER)
    d.ellipse([SPINE_X - 5, ny - 5, SPINE_X + 5, ny + 5], fill=NIGHT)
    # big number + tag + headline + deck
    put((100, y + 2), num, SANS_B(30), AMBER)
    put((170, y + 4), tag, SANS_B(12), CYAN)
    put((170, y + 22), head, SANS_B(25), WHITE)
    block(170, y + 56, deck, SANS(15), PANEL_X - 170 - 18, 20, GREY,
          limit=2)
    # right panel: illustration above, key figure below
    d.rounded_rectangle([PANEL_X, y + 4, RIGHT, y + 110], radius=8,
                        fill=PANEL, outline=PANEL_EDGE, width=1)
    mini(PANEL_X, y + 4, kind)
    sw = d.textlength(stat, font=SANS_B(19))
    put((PANEL_X + (PANEL_W - sw) / 2, y + 82), stat, SANS_B(19), AMBER)
    if i < 5:
        d.line([SPINE_X, y + PITCH - 6, SPINE_X, y + PITCH + 6],
               fill=SPINE, width=3)

# ------------------------------------------------------------------ footer
FY = 916
d.line([LEFT, FY, RIGHT, FY], fill=SPINE, width=1)
put((LEFT, FY + 12),
    "Sources: Reuters \u00b7 AP \u00b7 Bloomberg \u00b7 NASA \u00b7 India "
    "Meteorological Department \u00b7 European Commission",
    SANS(13), DIM)
put((LEFT, FY + 34),
    "All events of Thursday 19 November 2026.",
    SANS_B(13), GREY)

img.save("entry.png", format="PNG", optimize=True)
print("saved entry.png", img.size)

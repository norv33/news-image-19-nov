#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261119, version 2.

Design v2 is a broadsheet, deliberately unlike v1's dark-green storyboard
cards: warm ivory paper, a big serif masthead ("THE WORLD"), a crimson
dateline, a two-column front page (lead story + second story on the left,
four briefs on the right), a "BY THE NUMBERS" strip and a sources footer.
All six stories of Thursday 19 November 2026 are in it, with the date
named twice. Deterministic: same bytes every run.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 30

PAPER = (246, 241, 229)     # warm ivory newsprint
INK = (26, 24, 20)
CRIMSON = (155, 28, 28)
TEAL = (18, 77, 75)
GREY = (105, 100, 88)
RULE = (178, 170, 148)
SKY = (233, 229, 214)       # pale sky in the lead illustration
BROWN = (120, 72, 20)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSerif.ttf", s)
SANS_B = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", s)
SANS = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", s)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def text(xy, s, font, fill):
    d.text(xy, s, font=font, fill=fill)


def centre(y, s, font, fill):
    w = d.textlength(s, font=font)
    text(((W - w) / 2, y), s, font, fill)


def wrap(s, font, max_w):
    """Greedy word wrap; returns list of lines."""
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


def para(x, y, s, font, max_w, leading, fill, max_lines=None):
    """Draw wrapped paragraph; return y after the last line."""
    lines = wrap(s, font, max_w)
    if max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        text((x, y), ln, font, fill)
        y += leading
    return y


def rule(x0, x1, y, width=1, fill=RULE):
    d.line([x0, y, x1, y], fill=fill, width=width)


# ---------------------------------------------------------------- masthead
centre(22, "ONE DAY  \u00b7  SIX STORIES  \u00b7  FROM AROUND THE GLOBE",
       SANS_B(13), GREY)
rule(MARGIN, W - MARGIN, 46, 2, INK)
centre(56, "THE WORLD", SERIF_B(88), INK)
centre(150, "THURSDAY, 19 NOVEMBER 2026", SERIF_B(30), CRIMSON)
rule(MARGIN, W - MARGIN, 190, 1, INK)
rule(MARGIN, W - MARGIN, 194, 2, INK)

# ---------------------------------------------------------------- columns
TOP, BOTTOM = 210, 850
LEFT_X, LEFT_W = MARGIN, 562
RIGHT_X, RIGHT_W = 612, W - MARGIN - 612
d.line([602, TOP, 602, BOTTOM], fill=RULE, width=1)  # column divider

# ---------------------------------------------------------------- lead story
y = TOP
text((LEFT_X, y), "LEAD STORY", SANS_B(14), CRIMSON)
y += 24
y = para(LEFT_X, y, "THREE LEADERS, ONE TABLE", SERIF_B(42), LEFT_W, 50,
         INK, max_lines=2)
y += 4
y = para(LEFT_X, y,
         "Trump, Xi and Putin meet in Shenzhen today \u2014 the first-ever "
         "trilateral \u2014 with nuclear arms, Iran and Ukraine on the "
         "agenda.", SANS(16), LEFT_W, 21, (52, 48, 40), max_lines=3)
y += 10

# Summit illustration: three flags behind a long table.
IX, IY, IW, IH = LEFT_X, y, LEFT_W, 150
d.rectangle([IX, IY, IX + IW, IY + IH], fill=SKY, outline=RULE, width=1)
for cx, flag in ((IX + 90, "us"), (IX + IW // 2, "cn"), (IX + IW - 90, "ru")):
    d.line([cx, IY + 8, cx, IY + 96], fill=INK, width=3)
    fx, fy, fw, fh = cx + 2, IY + 8, 72, 44
    if flag == "us":
        d.rectangle([fx, fy, fx + fw, fy + fh], fill=WHITE, outline=INK,
                    width=1)
        for i in range(4):
            d.rectangle([fx, fy + i * 11, fx + fw, fy + i * 11 + 5],
                        fill=(178, 34, 52))
        d.rectangle([fx, fy, fx + 30, fy + 22], fill=(41, 98, 168))
        for sx in (fx + 7, fx + 17):
            for sy in (fy + 6, fy + 14):
                d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=WHITE)
    elif flag == "cn":
        d.rectangle([fx, fy, fx + fw, fy + fh], fill=(222, 41, 16),
                    outline=INK, width=1)
        d.ellipse([fx + 10, fy + 9, fx + 24, fy + 23], fill=(255, 222, 0))
        for sx, sy in ((fx + 34, fy + 8), (fx + 42, fy + 16),
                       (fx + 34, fy + 26)):
            d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(255, 222, 0))
    else:
        d.rectangle([fx, fy, fx + fw, fy + fh], fill=WHITE, outline=INK,
                    width=1)
        d.rectangle([fx, fy + 15, fx + fw, fy + 29], fill=(41, 98, 168))
        d.rectangle([fx, fy + 29, fx + fw, fy + fh], fill=(198, 52, 40))
# table
d.rectangle([IX + 30, IY + 100, IX + IW - 30, IY + 114], fill=BROWN)
d.rectangle([IX + 44, IY + 114, IX + 52, IY + IH - 4], fill=BROWN)
d.rectangle([IX + IW - 52, IY + 114, IX + IW - 44, IY + IH - 4], fill=BROWN)
y = IY + IH + 10
y = para(LEFT_X, y,
         "The summit is the first time the three leaders have sat down "
         "together. Markets and capitals alike are watching what, if "
         "anything, they agree.", SANS(14), LEFT_W, 19, (70, 66, 58),
         max_lines=3)

# ---------------------------------------------------------------- second story
y += 8
rule(LEFT_X, LEFT_X + LEFT_W, y, 1, RULE)
y += 12
text((LEFT_X, y), "CULTURE", SANS_B(13), CRIMSON)
y += 22
y = para(LEFT_X, y, "VICE CITY OPENS ITS DOORS", SERIF_B(29), LEFT_W, 35,
         INK, max_lines=2)
y += 2
y = para(LEFT_X, y,
         "Grand Theft Auto VI rolls out worldwide from midnight local time "
         "\u2014 13 years after GTA V \u2014 and already at 99 on Metacritic.",
         SANS(15), LEFT_W, 20, (52, 48, 40), max_lines=3)
y += 10

# Sunset skyline strip with a big VI.
SX, SY, SW, SH = LEFT_X, y, LEFT_W, 96
bands = [(255, 140, 60), (255, 110, 80), (220, 80, 120), (140, 60, 140)]
for i, c in enumerate(bands):
    d.rectangle([SX, SY + i * SH // 4, SX + SW, SY + (i + 1) * SH // 4],
                fill=c)
d.rectangle([SX, SY, SX + SW, SY + SH], outline=RULE, width=1)
for bx, bh in ((0, 34), (52, 52), (108, 40), (160, 62), (214, 46),
               (268, 58), (322, 38), (376, 54), (430, 42)):
    d.rectangle([SX + bx, SY + SH - bh, SX + bx + 46, SY + SH],
                fill=(28, 18, 40))
    for wy in range(SY + SH - bh + 8, SY + SH - 6, 12):
        for wx in (SX + bx + 8, SX + bx + 24):
            d.rectangle([wx, wy, wx + 6, wy + 5], fill=(255, 210, 63))
text((SX + SW - 92, SY + 12), "VI", SERIF_B(56), WHITE)

# ---------------------------------------------------------------- right column briefs
BRIEFS = [
    ("03", "ANTHROPIC\u2019S RECORD DEBUT",
     "Shares start trading on Nasdaq today under ANT after an $81.3bn IPO "
     "priced at $83 \u2014 the largest ever, at a ~$1.5tn value."),
    ("04", "AKVAN BEARS DOWN ON INDIA",
     "The cyclone strengthens to a very severe storm today; red alerts on "
     "the Andhra\u2013Odisha coast ahead of landfall due Friday."),
    ("05", "VOYAGER 1, ONE LIGHT-DAY OUT",
     "NASA marks the milestone today: the first human-made object 16bn "
     "miles away \u2014 a radio signal now takes a day to reach it."),
    ("06", "EU\u2019S \u20ac45BN LOAN GOES TO BERLIN",
     "Allies meet in Berlin today to discuss the Commission\u2019s \u20ac45bn "
     "Ukraine loan for 2027 \u2014 repaid only once Russia pays "
     "reparations."),
]
by = TOP
for i, (num, head, body) in enumerate(BRIEFS):
    if i:
        rule(RIGHT_X, RIGHT_X + RIGHT_W, by, 1, RULE)
        by += 12
    text((RIGHT_X, by), num, SERIF_B(22), CRIMSON)
    hy = by + 2
    hy = para(RIGHT_X + 44, hy, head, SERIF_B(19), RIGHT_W - 44, 23, INK,
              max_lines=2)
    by = para(RIGHT_X + 44, hy + 2, body, SANS(14), RIGHT_W - 44, 18,
              (52, 48, 40), max_lines=4)
    by += 12

# About this page: fills the foot of the right column honestly.
rule(RIGHT_X, RIGHT_X + RIGHT_W, by, 1, RULE)
by += 12
text((RIGHT_X, by), "ABOUT THIS PAGE", SANS_B(13), CRIMSON)
by += 22
by = para(RIGHT_X, by,
          "Six stories, chosen for consequence and breadth: one summit, "
          "one launch, one listing, one storm, one spacecraft, one loan. "
          "All events of Thursday 19 November 2026.",
          SANS(13), RIGHT_W, 18, (70, 66, 58), max_lines=5)

# ---------------------------------------------------------------- numbers strip
NY = 862
d.rectangle([MARGIN, NY, W - MARGIN, NY + 74], outline=INK, width=2)
d.line([MARGIN, NY + 3, W - MARGIN, NY + 3], fill=INK, width=1)
text((MARGIN + 14, NY + 12), "BY THE", SANS_B(13), CRIMSON)
text((MARGIN + 14, NY + 30), "NUMBERS", SANS_B(13), CRIMSON)
NUMBERS = [
    ("3", "leaders meet"),
    ("$81.3bn", "record IPO"),
    ("99", "GTA VI score"),
    ("16bn mi", "Voyager 1"),
    ("\u20ac45bn", "EU loan"),
]
col_x = MARGIN + 128
col_w = (W - MARGIN - col_x) // 5
for i, (num, lab) in enumerate(NUMBERS):
    cx = col_x + i * col_w
    text((cx, NY + 10), num, SERIF_B(26), INK)
    text((cx, NY + 46), lab, SANS(13), GREY)
    if i:
        d.line([cx - 12, NY + 12, cx - 12, NY + 62], fill=RULE, width=1)

# ---------------------------------------------------------------- footer
FY = 952
rule(MARGIN, W - MARGIN, FY, 1, RULE)
text((MARGIN, FY + 8), "ALSO TODAY \u2014", SANS_B(14), CRIMSON)
ax = MARGIN + d.textlength("ALSO TODAY \u2014 ", font=SANS_B(14))
text((ax, FY + 8),
     "APEC closes in Shenzhen \u00b7 Red alert in 7 Andhra districts \u00b7 "
     "GTA VI unlocks at midnight ET in the US", SANS(14), INK)
text((MARGIN, FY + 30),
     "Sources: Reuters \u00b7 AP \u00b7 Bloomberg \u00b7 NASA \u00b7 India "
     "Meteorological Department \u00b7 European Commission",
     SANS(12), GREY)
text((MARGIN, FY + 48),
     "All events of Thursday 19 November 2026.",
     SANS(12), GREY)

img.save("entry.png", format="PNG", optimize=True)
print("saved entry.png", img.size)

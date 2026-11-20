#!/usr/bin/env python3
"""Draw entry.png for news-image-20261119 v4: a Swiss typography poster.

White page, giant black type, red rules and numbers, pure typography -
no pictograms, no illustrations. 1024x1024, PIL + Liberation Sans
(DejaVu Sans fallback).
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 40
CW = W - 2 * MARGIN  # 944

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (214, 0, 28)
GREY = (110, 110, 110)

SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FALLBACK = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FALLBACK_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        alt = FALLBACK_BOLD if "Bold" in path else FALLBACK
        return ImageFont.truetype(alt, size)


def bold(size):
    return font(SANS_BOLD, size)


def regular(size):
    return font(SANS, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit width."""
    lines = []
    for chunk in text.split("\n"):
        words = chunk.split()
        line = ""
        for word in words:
            trial = (line + " " + word).strip()
            if draw.textlength(trial, font=fnt) <= width:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
    return lines


STORIES = [
    ("01", "SUMMIT", "THREE LEADERS, ONE TABLE",
     "Trump, Xi and Putin meet in Shenzhen today \u2014 the first-ever "
     "trilateral \u2014 with nuclear arms, Iran and Ukraine on the agenda."),
    ("02", "GAMES", "VICE CITY OPENS ITS DOORS",
     "Grand Theft Auto VI launches worldwide at midnight local time, "
     "13 years after GTA V \u2014 already at 99 on Metacritic."),
    ("03", "MARKETS", "ANTHROPIC\u2019S RECORD DEBUT",
     "Shares begin trading on Nasdaq as ANT after an $81.3bn IPO \u2014 "
     "the largest ever \u2014 valued near $1.5tn."),
    ("04", "WEATHER", "AKVAN BEARS DOWN ON INDIA",
     "The cyclone strengthens to a very severe storm; red alerts along "
     "the Andhra\u2013Odisha coast before landfall on Friday."),
    ("05", "SPACE", "VOYAGER 1, ONE LIGHT-DAY OUT",
     "NASA marks the milestone: the first human-made object 16bn miles "
     "out \u2014 a radio signal now takes a day to reach it."),
    ("06", "EUROPE", "EU\u2019S \u20ac45BN LOAN GOES TO BERLIN",
     "Allies meet in Berlin to discuss the Commission\u2019s \u20ac45bn "
     "Ukraine loan for 2027, repaid only once Russia pays reparations."),
]

NUMBERS = [
    ("3", "LEADERS IN SHENZHEN"),
    ("$81.3BN", "ANTHROPIC IPO"),
    ("99", "GTA VI \u00b7 METACRITIC"),
    ("16BN MI", "VOYAGER 1 FROM EARTH"),
    ("\u20ac45BN", "EU LOAN FOR UKRAINE"),
]


def main():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    # Outer frame.
    d.rectangle([28, 28, 996, 996], outline=BLACK, width=3)

    # Kicker row.
    d.rectangle([MARGIN, 44, MARGIN + 14, 58], fill=RED)
    d.text((MARGIN + 24, 38), "THE WORLD IN ONE DAY", font=bold(26), fill=BLACK)
    d.text((W - MARGIN, 38), "THURSDAY", font=bold(26), fill=BLACK, anchor="ra")

    # Giant date: black "19 NOVEMBER " + red "2026", fitted to full width.
    size = 130
    f_date = bold(size)
    while d.textlength("19 NOVEMBER 2026", font=f_date) > CW and size > 40:
        size -= 2
        f_date = bold(size)
    y_date = 74
    d.text((MARGIN, y_date), "19 NOVEMBER 2026", font=f_date, fill=BLACK)
    pre = d.textlength("19 NOVEMBER ", font=f_date)
    d.text((MARGIN + pre, y_date), "2026", font=f_date, fill=RED)

    # Thick red rule under the date.
    d.rectangle([MARGIN, 196, W - MARGIN, 206], fill=RED)

    # Subline.
    d.text((MARGIN, 216), "SIX STORIES FROM AROUND THE WORLD",
           font=bold(23), fill=BLACK)
    d.text((W - MARGIN, 216), "ONE DAY \u00b7 SIX STORIES",
           font=bold(23), fill=RED, anchor="ra")

    # 2x3 story grid with hairline rules.
    gx0, gy0 = MARGIN, 248
    col_w, row_h = CW // 2, 184
    d.line([(gx0 + col_w, gy0), (gx0 + col_w, gy0 + 3 * row_h)],
           fill=BLACK, width=2)
    for r in (1, 2):
        y = gy0 + r * row_h
        d.line([(gx0, y), (gx0 + CW, y)], fill=BLACK, width=2)

    for i, (num, tag, head, deck) in enumerate(STORIES):
        cx = gx0 + (i % 2) * col_w
        cy = gy0 + (i // 2) * row_h
        pad = 16
        # Big red index number, left column of the cell.
        d.text((cx + pad, cy + 12), num, font=bold(40), fill=RED)
        tx = cx + pad + 62
        tw = col_w - pad - 62 - pad
        # Red category tag, top right of the cell.
        d.text((cx + col_w - pad, cy + 16), tag, font=bold(15),
               fill=RED, anchor="ra")
        # Headline, up to two lines. The first line reserves room for the
        # red category tag at the top right, so the two never collide.
        f_head = bold(26)
        tagw = d.textlength(tag, font=bold(15))
        lines = wrap(d, head, f_head, tw - tagw - 12)[:2]
        hy = cy + 14
        for ln in lines:
            d.text((tx, hy), ln, font=f_head, fill=BLACK)
            hy += 31
        # Thin rule under the headline.
        d.line([(tx, hy + 4), (tx + tw, hy + 4)], fill=BLACK, width=2)
        # Deck, up to three lines.
        f_deck = regular(16)
        dlines = wrap(d, deck, f_deck, tw)[:3]
        dy = hy + 14
        for ln in dlines:
            d.text((tx, dy), ln, font=f_deck, fill=BLACK)
            dy += 21

    # "BY THE NUMBERS" label + black strip.
    ny = gy0 + 3 * row_h + 14
    d.text((MARGIN, ny), "BY THE NUMBERS", font=bold(18), fill=RED)
    sy = ny + 26
    d.rectangle([MARGIN, sy, W - MARGIN, sy + 88], fill=BLACK)
    col = CW / len(NUMBERS)
    f_num = bold(34)
    f_lab = bold(13)
    for j, (val, lab) in enumerate(NUMBERS):
        ccx = MARGIN + col * j + col / 2
        d.text((ccx, sy + 12), val, font=f_num, fill=WHITE, anchor="ma")
        d.text((ccx, sy + 56), lab, font=f_lab, fill=RED, anchor="ma")

    # "ALSO TODAY" line.
    ay = sy + 88 + 12
    d.text((MARGIN, ay), "ALSO TODAY \u2014 ", font=bold(16), fill=RED)
    off = d.textlength("ALSO TODAY \u2014 ", font=bold(16))
    d.text((MARGIN + off, ay),
           "APEC closes in Shenzhen \u00b7 Red alert in 7 Andhra districts "
           "\u00b7 GTA VI unlocks at midnight ET in the US",
           font=regular(16), fill=BLACK)

    # Footer: sources, single line.
    fy = ay + 26
    d.text((MARGIN, fy),
           "Sources: Reuters \u00b7 AP \u00b7 Bloomberg \u00b7 NASA \u00b7 "
           "India Meteorological Department \u00b7 European Commission \u2014 "
           "All events of Thursday 19 November 2026.",
           font=regular(13), fill=GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()

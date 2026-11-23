#!/usr/bin/env python3
"""Front page for Monday 23 November 2026, drawn as a 1024x1024 PNG.

Pillow only, no network, no files read except the fonts. Running it
twice writes the same bytes. Run from this directory:

    python3 draw_news.py

and it leaves entry.png beside itself. Every story below was checked
against reports dated 23 November 2026: each one either happened that
day or was first reported that day. Stories dated 20-22 November were
left out on purpose.
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

PAGE = 1024
PAPER = (245, 241, 230)
NAVY = (15, 42, 68)
GOLD = (201, 162, 39)
BOLD_TTF = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG_TTF = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def face(size, bold=True):
    return ImageFont.truetype(BOLD_TTF if bold else REG_TTF, size)


def fit_text(pen, s, fnt, width):
    """Split s into lines no wider than width pixels."""
    out, cur = [], ""
    for word in s.split():
        trial = f"{cur} {word}".strip()
        if pen.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def glyph(pen, cx, cy, name, hue):
    """A small white pictogram inside a coloured disc."""
    pen.ellipse([cx - 46, cy - 46, cx + 46, cy + 46], fill=hue)
    if name == "globe":
        pen.ellipse([cx - 30, cy - 30, cx + 30, cy + 30], fill="#2E86C1",
                    outline="white", width=3)
        pen.ellipse([cx - 18, cy - 20, cx + 2, cy - 2], fill="#27AE60")
        pen.ellipse([cx - 2, cy + 4, cx + 22, cy + 22], fill="#27AE60")
        pen.arc([cx - 30, cy - 30, cx + 30, cy + 30], 210, 330,
                fill="white", width=3)
    elif name == "ship":
        pen.rectangle([cx - 34, cy - 4, cx + 34, cy + 14], fill="white")
        pen.polygon([(cx - 34, cy + 14), (cx + 34, cy + 14),
                     (cx + 24, cy + 28), (cx - 24, cy + 28)], fill="#E8E8E8")
        pen.rectangle([cx - 22, cy - 20, cx - 4, cy - 4], fill="white")
        pen.rectangle([cx + 4, cy - 20, cx + 20, cy - 4], fill="white")
        pen.polygon([(cx + 14, cy - 42), (cx + 24, cy - 22), (cx + 4, cy - 22)],
                    fill="#FFC107")
        pen.polygon([(cx - 4, cy - 36), (cx + 4, cy - 22), (cx - 12, cy - 22)],
                    fill="#FF8C00")
    elif name == "cup":
        pts = []
        for i in range(10):
            ang = -math.pi / 2 + i * math.pi / 5
            rr = 38 if i % 2 == 0 else 16
            pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
        pen.polygon(pts, fill="#FFC107", outline="white", width=3)
        pen.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=hue)
    elif name == "blast":
        pts = []
        for i in range(12):
            ang = -math.pi / 2 + i * math.pi / 6
            rr = 40 if i % 2 == 0 else 18
            pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
        pen.polygon(pts, fill="#FFC107", outline="white", width=3)
        pen.rectangle([cx - 26, cy + 16, cx - 12, cy + 38], fill="white")
        pen.rectangle([cx - 6, cy + 22, cx + 6, cy + 38], fill="white")
        pen.rectangle([cx + 12, cy + 14, cx + 26, cy + 38], fill="white")
    elif name == "chart":
        pen.line([(cx - 30, cy + 24), (cx - 30, cy - 26)], fill="white", width=4)
        pen.line([(cx - 30, cy + 24), (cx + 32, cy + 24)], fill="white", width=4)
        pen.line([(cx - 24, cy - 14), (cx - 8, cy - 2), (cx + 6, cy - 10),
                  (cx + 26, cy + 18)], fill="#FF5252", width=6, joint="curve")
        pen.polygon([(cx + 26, cy + 18), (cx + 14, cy + 14), (cx + 22, cy + 28)],
                    fill="#FF5252")
    elif name == "sun":
        pen.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], fill="#FFC107",
                    outline="white", width=3)
        for i in range(8):
            ang = i * math.pi / 4
            pen.line([(cx + 24 * math.cos(ang), cy + 24 * math.sin(ang)),
                      (cx + 34 * math.cos(ang), cy + 34 * math.sin(ang))],
                     fill="white", width=4)


STORIES = [
    dict(place="MARKETS  •  SEOUL", hue="#7A1F2B",
         head=["KOSPI SINKS", "AGAIN"],
         body="Seoul shares fall 3.7% as the AI sell-off spreads across Asia.",
         mark="chart"),
    dict(place="LIBYA  •  BENGHAZI", hue="#B3261E",
         head=["UN SEEKS", "PROBE"],
         body="The UN demands an inquiry into drone strikes on ships off Libya.",
         mark="ship"),
    dict(place="UN  •  GENEVA", hue="#0E7A5F",
         head=["LETHAL AI", "TALKS GO ON"],
         body="Nations agree to keep negotiating limits on autonomous weapons.",
         mark="globe"),
    dict(place="FOOTBALL  •  ZURICH", hue="#1D4E89",
         head=["UK TO HOST", "2035 CUP"],
         body="FIFA is set to confirm the UK as host of the 2035 Women's World Cup.",
         mark="cup"),
    dict(place="IOWA  •  USA", hue="#8A6D00",
         head=["ARMY TO BLAST", "5 TONS"],
         body="The US Army will blow up unstable explosives, defying a court pause.",
         mark="blast"),
    dict(place="CLIMATE  •  ANTALYA", hue="#5B4A2E",
         head=["BLAME TURNS", "TO RIYADH"],
         body="Reports say Saudi influence helped sink the COP31 climate deal.",
         mark="sun"),
]

FOOTNOTE = ("Also: Taiwan's Taiex falls 0.9%  •  "
            "MSCI Asia Pacific 18% below its June peak")


def panel(pen, x, y, w, h, story):
    pen.rounded_rectangle([x, y, x + w, y + h], radius=16, fill="white",
                          outline="#D8D2C0", width=2)
    pen.rectangle([x + 16, y, x + w - 16, y + 7], fill=story["hue"])
    glyph(pen, x + 62, y + 64, story["mark"], story["hue"])
    pen.text((x + 124, y + 28), story["place"], font=face(18), fill=story["hue"])
    yy = y + 116
    for line in story["head"]:
        pen.text((x + 24, yy), line, font=face(32), fill="#111827")
        yy += 38
    yy = y + 196
    for line in fit_text(pen, story["body"], face(22, bold=False), w - 48):
        pen.text((x + 24, yy), line, font=face(22, bold=False), fill="#333333")
        yy += 28


def main():
    sheet = Image.new("RGB", (PAGE, PAGE), PAPER)
    pen = ImageDraw.Draw(sheet)
    pen.rectangle([0, 0, PAGE, 150], fill=NAVY)
    pen.rectangle([0, 150, PAGE, 156], fill=GOLD)
    pen.text((32, 24), "THE WORLD  •  ONE DAY  •  ONE IMAGE",
             font=face(24), fill=GOLD)
    pen.text((32, 52), "MONDAY 23 NOVEMBER 2026", font=face(48), fill="white")
    pen.text((32, 112), "The day's biggest stories, around the world",
             font=face(26, bold=False), fill="#D6DEE8")
    margin, gap = 18, 14
    tw = (PAGE - 2 * margin - gap) // 2
    th = 248
    top = 170
    for i, story in enumerate(STORIES):
        x = margin + (i % 2) * (tw + gap)
        y = top + (i // 2) * (th + gap)
        panel(pen, x, y, tw, th, story)
    pen.text((32, 954), FOOTNOTE, font=face(21, bold=False), fill="#555555")
    out = Path(__file__).resolve().parent / "entry.png"
    sheet.save(out, optimize=True)
    print("saved", out, sheet.size, out.stat().st_size, "bytes")


if __name__ == "__main__":
    main()

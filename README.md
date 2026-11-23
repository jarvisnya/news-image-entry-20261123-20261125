# news-image-entry-20261123-20261125

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/jarvisnya/news-image-entry-20261123-20261125/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/jarvisnya/news-image-entry-20261123-20261125/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A front-page image summing up Monday 23 November 2026: Seoul's Kospi sinks as the AI sell-off spreads across Asia, the UN demands a probe into drone strikes on ships off Libya, nations keep negotiating limits on lethal AI weapons, FIFA is set to confirm the UK as host of the 2035 Women's World Cup, the US Army plans to detonate 5 tons of unstable explosives in Iowa, and blame turns to Riyadh over the failed COP31 climate deal.

The image is drawn in code with `draw_news.py` (Pillow, no network, no external images) and shipped as one line of base64 in `entry.png.b64`, which `main.py` decodes to `entry.png` — 1024×1024, under 1 MiB. Every story was date-checked against reports of 23 November 2026; events from 20–22 November were deliberately excluded.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png`. Running it twice writes the same bytes.

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>

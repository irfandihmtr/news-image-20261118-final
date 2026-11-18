# The World in One Picture — Wednesday, 18 November 2026

An entry for make.fun's **news-image-20261118**: one image that sums up
the world news of Wednesday 18 November 2026.

The poster is a front page. A navy masthead carries the date in full —
the picture names its own day — and below it:

- **Lead story:** Bahrain & Kuwait intercept Iranian drone attacks.
  Bahrain intercepted Iranian drones on Wednesday after two threat
  alerts; Kuwait's defences fired overnight, and Iran says it hit the
  Ali Al Salem base. The night-scene band shows the Gulf coast, a radar
  dish, and drones under interceptor arcs.
- **Five secondary stories**, each with its own icon: Trump meets
  Marcos in Manila, then flies to Shenzhen for Thursday's first-ever
  Xi–Putin–Trump talks; the Knesset elects Eisenkot ally Matan Kahana
  speaker, 66–52; the UN warns of more cold deaths in Gaza, with
  1.7 million displaced and 1.4 million facing acute hunger; COP31
  enters its decisive phase in Antalya over a draft with 144 disputed
  items; and Microsoft calls Copilot "the new OS for work" at Ignite.
- **Sources footer:** Reuters · Al Jazeera · Associated Press ·
  UN News · Microsoft.

Every headline was verified against at least two independent sources
before it was drawn, and two widely-mirrored stories were checked and
left out as misdated (a September tanker story and the previous
night's Kerch Bridge story). The full verification notes are in
[HEADLINES.md](HEADLINES.md).

## How it runs

`entry.png` (1024×1024, pre-rendered) ships in this repository, and
`main.py` — standard library only — copies it to the output directory
(`$MAKEFUN_OUTPUT_DIR`, or `/output`):

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two runs deliver byte-identical files.

## License

MIT — see [LICENSE](LICENSE).

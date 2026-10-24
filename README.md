<a href="https://encs4101.birzeit.me"><img src="public/og.png" alt="ENCS4101 Embedded Systems Laboratory" width="100%"></a>

# ENCS4101 · Embedded Systems Laboratory

Step-by-step lab manual for ENCS4101 at Birzeit University: STM32 with STM32CubeIDE and the HAL library, from GPIO and interrupts to timers, PWM, motors, ADC, I²C and UART.

**[Open the manual](https://encs4101.birzeit.me)** · [PDF](https://encs4101.birzeit.me/ENCS4101-Manual.pdf) · [Setup guide](https://encs4101.birzeit.me/setup) · [All labs](https://birzeit.me)

## Run it locally

Requires [Node.js](https://nodejs.org) 24 and npm.

```sh
git clone https://github.com/ECE-Birzeit/encs4101.git
cd encs4101
npm ci
npm run dev        # http://localhost:5173, reloads as you edit
```

```sh
npm run build      # outputs to .vitepress/dist, fails on dead links
npm run preview    # serve the built site
```

## Project layout

| Path | Contents |
|:--|:--|
| `index.md` | Home page |
| `setup.md` | One-time STM32CubeIDE setup, shared by every experiment |
| `experiments/` | One page per experiment, plus the index table |
| `snippets/exp<N>/` | C source included into pages with `<<< @/snippets/...` |
| `public/images/exp<N>/` | Figures, exported from the LaTeX manual's `media/` |
| `public/ENCS4101-Manual.pdf` | Built copy of the department manual |
| `.vitepress/config.mts` | Site config: nav, sidebar, search, link previews |

The LaTeX sources for the department manual live in a separate repository, cloned into `embedded_systems_lab/` (gitignored). Figures are copied from its `media/experiment<N>_figures/` into `public/images/exp<N>/` with kebab-case names, and `document.pdf` is copied to `public/ENCS4101-Manual.pdf`.

## Contributing

Found a mistake? Click **Edit this page on GitHub** at the bottom of any page, or [open an issue](https://github.com/ECE-Birzeit/encs4101/issues/new/choose). The [contributing guide](https://github.com/ECE-Birzeit/.github/blob/main/CONTRIBUTING.md) covers writing style and pull requests.

## Deployment

`.github/workflows/deploy.yml` builds and deploys to GitHub Pages on every push to `main`, so merged changes are live within a couple of minutes at [encs4101.birzeit.me](https://encs4101.birzeit.me).

## License

The written content is licensed under [CC BY 4.0](LICENSE): you may share and adapt it, including for your own course, as long as you credit the source. Code, meaning `snippets/` and the site code (`.vitepress/`, `.github/`), is licensed under [MIT](LICENSE-CODE). © 2026 [Mohammad Abu-Shelbaia](https://mabushelbaia.com).

Not covered by either license, and still owned by their authors:

- `public/ENCS4101-Manual.pdf`, the department's manual
- `public/images/`, figures taken from the department's manual

The Birzeit University name and logo are the university's; they are not licensed here. Screenshots of third-party software, and product names and logos, belong to their respective owners.

---

<sub>Part of [ECE Lab Manuals](https://birzeit.me) · Maintained by [Mohammad Abu-Shelbaia](https://mabushelbaia.com)</sub>

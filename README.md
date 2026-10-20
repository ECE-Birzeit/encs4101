# ENCS4101 Embedded Systems Lab

Student site for the ENCS4101 Embedded Systems Laboratory (STM32, C) at Birzeit University, built with [VitePress](https://vitepress.dev).

## Development

```sh
npm install
npm run dev       # dev server with hot reload at http://localhost:5173
```

## Build

```sh
npm run build     # outputs to .vitepress/dist (fails on dead links)
npm run preview   # serve the built site locally
```

To build for a sub-path (e.g. a GitHub project site at `/<repo>/`):

```sh
BASE_PATH=/encs4101/ npm run build
```

## Deploying

`.github/workflows/deploy.yml` builds and deploys to GitHub Pages on every push to `main`. In the repository settings, set **Pages → Source** to **GitHub Actions**. The workflow sets `BASE_PATH` from the Pages configuration, so it works both as a project site and with a custom domain.

## Layout

| Path | Contents |
| --- | --- |
| `index.md` | Home page (hero + features) |
| `setup.md` | One-time STM32CubeIDE setup, shared by every experiment |
| `experiments/` | One page per experiment, plus the index table |
| `snippets/exp<N>/` | C source included into the pages with `<<< @/snippets/...` |
| `public/images/exp<N>/` | Figures, exported from the LaTeX manual's `media/` |
| `public/ENCS4101-Manual.pdf` | Built copy of the original manual |

### The manual sources

The LaTeX sources for the department manual live in a separate repository, cloned
into `embedded_systems_lab/` (gitignored here). Figures are copied out of its
`media/experiment<N>_figures/` into `public/images/exp<N>/` with kebab-case names,
and `document.pdf` is copied to `public/ENCS4101-Manual.pdf`.

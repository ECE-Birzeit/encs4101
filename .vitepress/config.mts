import { defineConfig } from 'vitepress'
import { withPwa } from '@vite-pwa/vitepress'
import { linkPreviews } from './og.mts'
import { sidebar } from './lab.mts'
import { fileURLToPath } from 'node:url'

const srcDir = fileURLToPath(new URL('..', import.meta.url))

// Per-experiment link previews, drawn at build time (see og.mts)
const og = linkPreviews({ code: 'ENCS4101', name: 'Embedded Systems Laboratory', host: 'encs4101.birzeit.me', accent: '#38bdf8', platform: 'STM32 · CubeIDE · HAL' })

// BASE_PATH is set by the GitHub Pages workflow ("/repo-name/" or "/" with a custom domain).
const base = process.env.BASE_PATH || '/'

export default withPwa(defineConfig({
  base,
  lang: 'en-US',
  title: 'ENCS4101 Embedded Systems Lab',
  description:
    'Step-by-step STM32 guides for the ENCS4101 Embedded Systems Laboratory at Birzeit University.',
  srcExclude: ['README.md', 'embedded_systems_lab/**'],
  cleanUrls: true,
  lastUpdated: true,

  head: [
    // .ico first for browsers and tools without SVG favicon support; the SVG wins where it is supported.
    ['link', { rel: 'icon', href: `${base}favicon.ico`, sizes: 'any' }],
    ['link', { rel: 'icon', type: 'image/svg+xml', href: `${base}favicon.svg` }],
    ['link', { rel: 'apple-touch-icon', href: `${base}apple-touch-icon.png` }],
    ['meta', { name: 'theme-color', content: '#0369a1' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:site_name', content: 'ECE Labs · Birzeit University' }],
    ...og.head,
    ['script', { async: '', src: 'https://www.googletagmanager.com/gtag/js?id=G-K834Q72PP9' }],
    [
      'script',
      {},
      `window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-K834Q72PP9');`,
    ],
  ],

  sitemap: { hostname: 'https://encs4101.birzeit.me/' },

  buildEnd: og.buildEnd,

  // Link previews: per-page title, the page's (or site's) description, and canonical URL.
  transformHead({ pageData, siteData }) {
    const page = pageData.frontmatter.layout === 'home' ? '' : pageData.title
    const path = pageData.relativePath.replace(/(^|\/)index\.md$/, '$1').replace(/\.md$/, '')
    return [
      ...og.transformHead({ pageData } as any),
      ['meta', { property: 'og:title', content: page ? `${page} · ENCS4101` : 'ENCS4101 Embedded Systems Laboratory' }],
      ['meta', { property: 'og:description', content: pageData.frontmatter.description || pageData.description || siteData.description }],
      ['meta', { property: 'og:url', content: `https://encs4101.birzeit.me/${path}` }],
    ]
  },

  themeConfig: {
    logo: '/favicon.svg',
    siteTitle: 'ENCS4101-BZU',

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Experiments', link: '/experiments/', activeMatch: '/experiments/' },
      { text: 'All labs', link: 'https://birzeit.me/' },
    ],

    // Built from the pages (see lab.mts): adding an experiment or a setup page is the only step
    sidebar: sidebar(srcDir, {
      downloads: [
            { text: 'STM32CubeIDE', link: 'https://www.st.com/en/development-tools/stm32cubeide.html' },
            { text: 'STM32CubeMX', link: 'https://www.st.com/en/development-tools/stm32cubemx.html' },
            { text: 'STM32CubeProgrammer', link: 'https://www.st.com/en/development-tools/stm32cubeprog.html' },
            { text: 'PuTTY (UART labs)', link: 'https://www.putty.org/' },
            // `base` by hand: a sidebar item with target '_blank' counts as external,
            // so VitePress does not prefix it for us.
            { text: 'Full Lab Manual (PDF)', link: `${base}ENCS4101-Manual.pdf`, target: '_blank' },
      ],
      docs: [
            { text: 'RM0090 — F407 Reference Manual', link: 'https://www.st.com/resource/en/reference_manual/rm0090-stm32f405415-stm32f407417-stm32f427437-and-stm32f429439-advanced-armbased-32bit-mcus-stmicroelectronics.pdf' },
            { text: 'RM0383 — F411 Reference Manual', link: 'https://www.st.com/resource/en/reference_manual/rm0383-stm32f411xce-advanced-armbased-32bit-mcus-stmicroelectronics.pdf' },
            { text: 'UM1725 — STM32F4 HAL Guide', link: 'https://www.st.com/resource/en/user_manual/um1725-description-of-stm32f4-hal-and-lowlayer-drivers-stmicroelectronics.pdf' },
            { text: 'F407 Discovery Board', link: 'https://www.st.com/en/evaluation-tools/stm32f4discovery.html' },
            { text: 'F411 Nucleo-64 Board', link: 'https://www.st.com/en/evaluation-tools/nucleo-f411re.html' },
            { text: 'STM32CubeIDE User Guide', link: 'https://www.st.com/resource/en/user_manual/um2609-stm32cubeide-user-guide-stmicroelectronics.pdf' },
            { text: 'Arm Cortex-M4 Generic User Guide', link: 'https://developer.arm.com/documentation/dui0553/latest/' },
            { text: 'HD44780 LCD Datasheet', link: 'https://www.sparkfun.com/datasheets/LCD/HD44780.pdf' },
            { text: 'PCF8574 Datasheet', link: 'https://www.ti.com/lit/ds/symlink/pcf8574.pdf' },
            { text: 'AN4073 — STM32F4 ADC Accuracy', link: 'https://www.st.com/resource/en/application_note/an4073-how-to-improve-adc-accuracy-when-using-stm32f2xx-and-stm32f4xx-microcontrollers-stmicroelectronics.pdf' },
      ],
    }),

    outline: { level: [2, 3] },

    search: { provider: 'local' },

    editLink: {
      pattern: 'https://github.com/ECE-Birzeit/encs4101/edit/main/:path',
      text: 'Edit this page on GitHub',
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/ECE-Birzeit/encs4101' },
    ],

    footer: {
      message: 'ENCS4101 · Embedded Systems Laboratory',
      copyright: 'Developed by <a href="https://mabushelbaia.com" target="_blank">Mohammad Abu-Shelbaia</a>',
    },
  },

  // Installable, offline-capable app. Icons are rendered from favicon.svg (the sidebar logo).
  pwa: {
    registerType: 'autoUpdate',
    manifest: {
      name: 'ENCS4101 Embedded Systems Laboratory',
      short_name: 'ENCS4101',
      description: 'Step-by-step STM32 guides for the ENCS4101 Embedded Systems Laboratory at Birzeit University.',
      theme_color: '#0369a1',
      background_color: '#ffffff',
      display: 'standalone',
      scope: base,
      start_url: base,
      icons: [
        { src: `${base}icons/pwa-192x192.png`, sizes: '192x192', type: 'image/png' },
        { src: `${base}icons/pwa-512x512.png`, sizes: '512x512', type: 'image/png' },
        { src: `${base}icons/maskable-512x512.png`, sizes: '512x512', type: 'image/png', purpose: 'maskable' },
        { src: `${base}favicon.svg`, sizes: 'any', type: 'image/svg+xml' },
      ],
    },
    workbox: {
      // The manual PDF is left out: it is too large to precache, and the guides do not need it offline.
      globPatterns: ['**/*.{css,js,html,svg,png,jpg,jpeg,webp,ico,txt,woff2}'],
      // Link-preview images are for chat apps and search engines, not for reading offline
      globIgnores: ['og/**'],
      maximumFileSizeToCacheInBytes: 5000000,
    },
    experimental: {
      includeAllowlist: true,
    },
  },
}))

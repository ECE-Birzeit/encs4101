// https://vitepress.dev/guide/custom-theme
import { h } from 'vue'
import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import './custom.css'

import RegisterSW from './components/RegisterSW.vue'
import ContinueReading from './components/ContinueReading.vue'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'home-hero-actions-after': () => h(ContinueReading, { lab: 'encs4101', mode: 'card' }),
      'layout-bottom': () => [h(RegisterSW), h(ContinueReading, { lab: 'encs4101', mode: 'track' })],
    })
  },
} satisfies Theme

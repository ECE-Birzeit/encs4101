---
layout: home

hero:
  name: ENCS4101
  text: Embedded Systems Laboratory
  tagline: Department of Electrical & Computer Engineering · Birzeit University
  actions:
    - theme: brand
      text: Explore Experiments
      link: /experiments/
    - theme: alt
      text: Download Full Manual
      # Relative on purpose: VitePress doesn't add `base` to non-page links in hero actions.
      link: ./ENCS4101-Manual.pdf
      target: _blank
    - theme: alt
      text: Setup Guide
      link: /setup

features:
  - icon:
      src: /icons/chip.svg
      alt: Microcontroller
      width: 28
      height: 28
      wrap: true
    title: STM32 from the Ground Up
    details: Configure clocks, GPIOs and interrupts with STM32CubeIDE and the HAL library, then drop below it in the final lab and drive the peripheral registers directly.
  - icon:
      src: /icons/signal.svg
      alt: Signal
      width: 28
      height: 28
      wrap: true
    title: Timers, PWM and Motors
    details: Generate precise timing with the hardware timers, then use it to read an encoder and to drive DC and stepper motors through real driver ICs.
  - icon:
      src: /icons/bus.svg
      alt: Serial bus
      width: 28
      height: 28
      wrap: true
    title: Sensors and Serial Buses
    details: Read analog sensors with the ADC and talk to the outside world over I²C and UART, with an LCD and a keypad as your user interface.
---

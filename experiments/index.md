# Experiments

Each guide is a step-by-step replacement for the matching chapter of the [department manual](/ENCS4101-Manual.pdf){target="_blank"}, written for current STM32CubeIDE. Linked experiments are ready, and the rest are coming soon. Finish the [Setup Guide](/setup) before your first lab.

| No. | Experiment | Topics |
| :-: | --- | --- |
| 1 | [GPIO, Switch Debouncing and Interrupts](./exp1-gpio) | GPIO input/output modes, push-pull vs open-drain, EXTI, NVIC, software debouncing with `HAL_GetTick()` |
| 2 | [LCD, I2C and Keypad](./exp2-lcd-keypad) | HD44780 character LCD, PCF8574 I²C expander, 4×4 matrix keypad scanning from `SysTick_Handler` |
| 3 | ADC and Analog Sensor Interfacing | ADC principles, resolution and sampling time, potentiometer / LDR / temperature sensors, showing readings on the LCD |
| 4 | Timer Configuration and Output Compare | Timer clock tree, prescaler and period, update interrupts, output compare mode, generating a variable frequency |
| 5 | DC Motor Control and PWM | PWM generation, duty cycle and speed, the L298 H-bridge, direction control |
| 6 | Rotary Encoder Interface | Incremental encoders, quadrature signals, the timer's encoder mode, computing position and speed |
| 7 | Stepper Motor Control | Full-step and half-step sequences, the ULN2003 driver, position, speed and direction |
| 8 | UART Protocol | Framing, baud rate and error, `HAL_UART_Transmit` / `Receive`, interrupt-driven reception, a serial terminal |
| 9 | Bare Metal Programming | Driving RCC and GPIO registers directly, no HAL, memory-mapped peripherals, what CubeMX generates for you |

::: info
Lab tasks and pre-lab questions are graded by your TA during the session. The **Task** section at the end of each guide is the work you hand in, not a worked solution.
:::

## How each guide is laid out

Every page follows the same shape, matching the manual:

- **Objectives** and **Pre-Lab** — what to read and answer *before* you come in.
- **Theory** — the background you need, with the figures from the manual.
- **Materials** — what to collect from the lab technician.
- **Relevant HAL APIs** — the handful of functions this experiment needs.
- **Procedure** — hardware wiring, then CubeMX configuration, then code.
- **After the lab** — what to observe and the questions to answer.
- **Task** — the hand-in work.

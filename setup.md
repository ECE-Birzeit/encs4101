# Setup Guide

This page gets your machine ready for every lab: install STM32CubeIDE, create a project the same way each week, and learn the build / flash / debug loop you will use in all nine experiments. Do this **before** your first lab session — the download is around 2 GB.

::: tip Why this page exists
Every experiment starts with "create a new STM32 project and configure the clock". That is written out once here instead of nine times. Each experiment page links back to the relevant section.
:::

## What you need

| | Minimum | Recommended |
| --- | --- | --- |
| RAM | 4 GB | 8 GB or more |
| Free disk | 6 GB | 10 GB |
| OS | Windows 10/11 64-bit, macOS, or a 64-bit Linux distribution | |
| Board | STM32F407VG Discovery **or** STM32F411RE Nucleo-64 | |
| USB cable | Mini-USB (Discovery) / Micro-USB (Nucleo) — a **data** cable, not charge-only | |

You do not need to install a toolchain or a JDK separately. STM32CubeIDE ships with the Arm GCC compiler, the ST-LINK drivers and its own Java runtime.

## 1. Install STM32CubeIDE

1. Go to [st.com/stm32cubeide](https://www.st.com/en/development-tools/stm32cubeide.html) and download the installer for your OS. You have to create a free myST account, or use the "Download as a guest" link.
2. Install it:
   - **Windows:** run the `.exe`. Accept the **ST-LINK**, **SEGGER J-Link** and **ST-LINK server** driver prompts that appear during the install — without them the board will not be detected.
   - **macOS:** open the `.dmg` and run the installer package.
   - **Linux:** unzip the archive and run the `.sh` installer. On Debian/Ubuntu install the udev rules it offers; on other distributions copy them from `/opt/st/stm32cubeide_*/drivers/rules/` into `/etc/udev/rules.d/` and run `sudo udevadm control --reload-rules`.
3. Launch it. Choose a **workspace** folder — a path with **no spaces and no non-English characters**, e.g. `C:\STM32\workspace`.
4. The first time you create a project, CubeIDE downloads the **STM32Cube MCU package** for your family (F4). This is a few hundred megabytes. Let it finish.

::: warning Keep paths short and ASCII-only
The Arm toolchain invokes long command lines. On Windows, workspaces under `C:\Users\<name with spaces>\OneDrive\…` cause builds to fail with confusing "file not found" errors. Use `C:\STM32\workspace`.
:::

## 2. Know your board

The two boards used in the lab differ in which pins are free and how they are clocked.

| | STM32F407VG Discovery | STM32F411RE Nucleo-64 |
| --- | --- | --- |
| MCU to select in the wizard | `STM32F407VGTx` | `STM32F411RETx` |
| Max HCLK | 168 MHz | 100 MHz |
| On-board crystal | 8 MHz HSE | 8 MHz MCO from ST-LINK |
| Built-in LEDs | PD12–PD15 | PA5 (LD2) |
| Built-in button | PA0 (blue, active high) | PC13 (active **low**) |
| **Pins to avoid** | PA13, PA14 (SWD) | PA2, PA3 (ST-LINK VCP), PA13, PA14 (SWD), PC14, PC15 (LSE) |

::: danger Never use PA13 / PA14
These are the SWDIO and SWCLK debug pins. If you assign them to something else and flash the board, the debugger can no longer connect. Recovering needs a "connect under reset" flash.
:::

## 3. Create a lab project

Every experiment starts with a new project created **exactly** this way. Each experiment page tells you which name to use.

1. **File → New → STM32 Project**. The target selector opens (first run is slow — it fetches the MCU database).
2. In the **Part Number Search** box, type your MCU (`STM32F407VGTx` or `STM32F411RETx`), select it in the list on the right, and click **Next**.

   ::: tip Or pick the board
   The **Board Selector** tab lets you choose `STM32F407G-DISC1` or `NUCLEO-F411RE` instead. If you do, answer **Yes** to "Initialize all peripherals with their default mode" only when you want the on-board LEDs and button pre-configured. The experiments here assume a plain MCU-based project, so **No** is the safer answer.
   :::

3. Fill in the form:

   | Field | Value |
   | --- | --- |
   | Project Name | The name on the experiment page, e.g. `Exp1_Counter` |
   | Location | Your workspace, no spaces |
   | Targeted Language | **C** |
   | Targeted Binary Type | **Executable** |
   | Targeted Project Type | **STM32Cube** |

   ::: danger Targeted Project Type must be STM32Cube
   **Empty** gives you a bare project with no HAL and no `.ioc` configuration file. Every experiment except [Experiment 9](/experiments/) needs **STM32Cube**.
   :::

4. Click **Finish**. Answer **Yes** to "Open Associated Perspective?". The `.ioc` **Device Configuration Tool** opens — this is where all pin and peripheral configuration happens.

### Configure the clock

Do this in every project, before anything else.

1. Open the **RCC** entry under *System Core* in the left-hand list.
2. Set **High Speed Clock (HSE)** to:
   - **Crystal/Ceramic Resonator** on the F407 Discovery.
   - **BYPASS Clock Source** on the F411 Nucleo (the 8 MHz comes from the ST-LINK, not a crystal).
3. Switch to the **Clock Configuration** tab.
4. Type the target frequency into the **HCLK (MHz)** box — `168` for the F407, `100` for the F411 — and press <kbd>Enter</kbd>. Answer **Yes** when CubeMX offers to solve the PLL settings for you. It fills in every prescaler automatically.

::: details Why bother, if the internal oscillator works?
The internal HSI is a factory-trimmed RC oscillator: it runs at 16 MHz ±1 % and drifts with temperature. That is fine for blinking an LED and not fine for UART baud rates ([Experiment 8](/experiments/)) or timer-derived frequencies ([Experiment 4](/experiments/)). The HSE crystal is accurate to a few tens of ppm.
:::

### Generate the code

After any change in the `.ioc` file: **Project → Generate Code** (or just save the `.ioc` with <kbd>Ctrl</kbd>+<kbd>S</kbd> and accept the prompt).

CubeMX writes `main.c`, `stm32f4xx_hal_msp.c`, `stm32f4xx_it.c` and the HAL drivers under `Drivers/`.

::: danger Only write between the USER CODE markers
Generated files are full of comment pairs like this:

```c
/* USER CODE BEGIN 2 */

/* USER CODE END 2 */
```

Code **inside** a pair survives regeneration. Code **outside** one is deleted the next time you generate. Every snippet on the experiment pages tells you which marker pair it belongs in.
:::

## 4. Build, flash and debug

| Action | Button / shortcut | What it does |
| --- | --- | --- |
| **Build** | hammer icon, <kbd>Ctrl</kbd>+<kbd>B</kbd> | Compiles to `Debug/<project>.elf` |
| **Run** | green ▶ | Flashes the board and runs it free |
| **Debug** | green 🐞 | Flashes, halts at `main()`, opens the Debug perspective |

The first **Run** or **Debug** opens a launch-configuration dialog. The defaults (ST-LINK, SWD, "Software system reset") are correct — click **OK**.

### The debug views you will actually use

The experiments ask you to inspect registers and variables live. All four are under **Window → Show View** while a debug session is running:

- **Live Expressions** — watch a variable change *while the target runs*, no breakpoints needed. This is the one you want for `buttonPressCount` in Experiment 1. Add an expression with the green **+**.
- **SFRs** — the peripheral registers by name. Expanding `GPIOD → ODR` shows the output data register bit by bit.
- **Breakpoints** — double-click in the left margin of the editor to set one.
- **Expressions / Variables** — values at the current halt point only.

::: tip Live Expressions needs optimisation off
Lab projects default to `-Og`, which is fine. If a variable shows `<optimized out>`, check **Project → Properties → C/C++ Build → Settings → Optimization** and set it to **-O0** or **-Og**, and make sure the variable is `volatile` if an ISR writes it.
:::

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `No ST-LINK detected` / `Target is not responding` | Try another USB cable — many are charge-only. On the F407 Discovery use the **mini-USB** port marked ST-LINK, not the micro-USB OTG port. |
| Board worked, now the debugger cannot connect | You probably reassigned PA13/PA14, or your code reconfigures them. In the launch config, set **Reset behaviour → Connect under reset**, flash a clean project, then fix the `.ioc`. |
| ST-LINK firmware is too old | **Help → ST-LINK Upgrade**, then **Open in update mode → Upgrade**. |
| Build fails with `undefined reference to HAL_...` | The peripheral is not enabled in the `.ioc`, so its HAL module was never compiled in. Enable it and regenerate. |
| My code disappeared after generating | It was outside a `USER CODE BEGIN/END` pair. Recover it from **local history**: right-click the file → **Compare With → Local History**. |
| Linux: board shows up only with `sudo` | The udev rules are missing. See step 1. |
| `arm-none-eabi-gcc: not found` after a CubeIDE update | **Help → Check for Updates**, then rebuild the index with **Project → Clean**. |
| Changes in the `.ioc` have no effect | You edited the `.ioc` but did not regenerate. **Project → Generate Code**. |

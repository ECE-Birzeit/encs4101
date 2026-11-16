"""Draws the header pinouts of the two lab boards as SVGs, top and bottom view.

  F407 Discovery (MB997):  P1 / P2, from ST UM1472, Table 5 and the top-layout figure.
  F411 Nucleo-64 (MB1136): CN7 / CN10 (ST morpho) with the Arduino names, from ST UM1724,
                           Table 29, Table 16 and the solder-bridge defaults (board C-02 or later).

On both boards pin 1 is the square pad at the ST-LINK end, and odd pins are in the left column
of each header (top view). The bottom view flips the board left-to-right.

Run from the repo root:  python3 scripts/draw-pinouts.py
Writes public/images/pinout/<board>-top.svg and <board>-bottom.svg."""
import sys
from html import escape

OUT_DIR = sys.argv[1] if len(sys.argv) > 1 else 'public/images/pinout'

# category -> (fill, text colour)
CAT = {
    'gnd':   ('#1f2328', '#ffffff'),
    'pwr':   ('#c62828', '#ffffff'),
    'free':  ('#f08c00', '#ffffff'),
    'board': ('#0f8f80', '#ffffff'),
    'dbg':   ('#8d6e63', '#ffffff'),
    'nc':    ('#c3c7cc', '#4b5158'),
}
TAG = {  # tag kind -> (fill, stroke, text)
    'use':  ('#d7f1ec', '#0f8f80', '#0b5f55'),
    'adc':  ('#fde9a8', '#d9a400', '#6b5100'),
    'tim':  ('#ffffff', '#f08c00', '#a35e00'),
    'com':  ('#e6e3fb', '#7b6fd6', '#40368f'),
    'ard':  ('#dbeafe', '#2563eb', '#1e3a8a'),
    'note': ('#eef0f2', '#c3c7cc', '#4b5158'),
}

def pin(name, cat, *tags):
    return (name, cat, list(tags))

def g(name, *tags):  # free GPIO
    return pin(name, 'free', *tags)

def b(name, *tags):  # GPIO already wired to an on-board part
    return pin(name, 'board', *tags)

def pw(name):
    return pin(name, 'pwr')

GND, NC = pin('GND', 'gnd'), pin('NC', 'nc')

# ---------------------------------------------------------------- F407 Discovery
DISCO_P1 = [
    (GND, GND),
    (pw('VDD'), pw('VDD')),
    (GND, pin('NRST', 'dbg', ('note', 'RESET'))),
    (g('PC1', ('adc', 'ADC IN11')), b('PC0', ('use', 'USB PWR EN'), ('adc', 'ADC IN10'))),
    (b('PC3', ('use', 'MIC DOUT'), ('adc', 'ADC IN13')), g('PC2', ('adc', 'ADC IN12'))),
    (g('PA1', ('adc', 'ADC IN1'), ('tim', 'TIM2_CH2')), b('PA0', ('use', 'USER BTN'), ('adc', 'ADC IN0'))),
    (g('PA3', ('adc', 'ADC IN3'), ('com', 'USART2 RX')), g('PA2', ('adc', 'ADC IN2'), ('com', 'USART2 TX'))),
    (b('PA5', ('use', 'ACCEL SCK'), ('adc', 'ADC IN5')), b('PA4', ('use', 'AUDIO WS'), ('adc', 'ADC IN4'))),
    (b('PA7', ('use', 'ACCEL MOSI'), ('adc', 'ADC IN7')), b('PA6', ('use', 'ACCEL MISO'), ('adc', 'ADC IN6'))),
    (g('PC5', ('adc', 'ADC IN15')), g('PC4', ('adc', 'ADC IN14'))),
    (g('PB1', ('adc', 'ADC IN9'), ('tim', 'TIM3_CH4')), g('PB0', ('adc', 'ADC IN8'), ('tim', 'TIM3_CH3'))),
    (GND, pin('PB2', 'nc', ('note', 'BOOT1'))),
    (g('PE7'), g('PE8')),
    (g('PE9', ('tim', 'TIM1_CH1')), g('PE10')),
    (g('PE11', ('tim', 'TIM1_CH2')), g('PE12')),
    (g('PE13', ('tim', 'TIM1_CH3')), g('PE14', ('tim', 'TIM1_CH4'))),
    (g('PE15'), b('PB10', ('use', 'MIC CLK'), ('com', 'I2C2 SCL'))),
    (g('PB11', ('com', 'I2C2 SDA')), g('PB12')),
    (g('PB13', ('com', 'SPI2 SCK')), g('PB14', ('com', 'SPI2 MISO'))),
    (g('PB15', ('com', 'SPI2 MOSI')), g('PD8', ('com', 'USART3 TX'))),
    (g('PD9', ('com', 'USART3 RX')), g('PD10')),
    (g('PD11'), b('PD12', ('use', 'LED GREEN'), ('tim', 'TIM4_CH1'))),
    (b('PD13', ('use', 'LED ORANGE'), ('tim', 'TIM4_CH2')), b('PD14', ('use', 'LED RED'), ('tim', 'TIM4_CH3'))),
    (b('PD15', ('use', 'LED BLUE'), ('tim', 'TIM4_CH4')), NC),
    (GND, GND),
]

DISCO_P2 = [
    (GND, GND),
    (pw('5V'), pw('5V')),
    (pw('3V'), pw('3V')),
    (pin('PH0', 'nc', ('note', '8 MHz XTAL')), pin('PH1', 'nc', ('note', '8 MHz XTAL'))),
    (pin('PC14', 'nc', ('note', '32 kHz XTAL')), pin('PC15', 'nc', ('note', '32 kHz XTAL'))),
    (g('PE6', ('tim', 'TIM9_CH2')), g('PC13')),
    (g('PE4'), g('PE5', ('tim', 'TIM9_CH1'))),
    (g('PE2'), b('PE3', ('use', 'ACCEL CS'))),
    (b('PE0', ('use', 'ACCEL INT1')), b('PE1', ('use', 'ACCEL INT2'))),
    (g('PB8', ('tim', 'TIM4_CH3'), ('com', 'I2C1 SCL')), b('PB9', ('use', 'AUDIO SDA'), ('tim', 'TIM4_CH4'))),
    (pin('BOOT0', 'dbg'), pw('VDD')),
    (b('PB6', ('use', 'AUDIO SCL'), ('com', 'I2C1 SCL')), g('PB7', ('com', 'I2C1 SDA'), ('tim', 'TIM4_CH2'))),
    (g('PB4', ('tim', 'TIM3_CH1')), g('PB5', ('tim', 'TIM3_CH2'))),
    (g('PD7'), pin('PB3', 'dbg', ('note', 'SWO'), ('tim', 'TIM2_CH2'))),
    (b('PD5', ('use', 'USB OVERCURR')), g('PD6')),
    (g('PD3'), b('PD4', ('use', 'AUDIO RESET'))),
    (g('PD1'), g('PD2')),
    (b('PC12', ('use', 'AUDIO SD')), g('PD0')),
    (b('PC10', ('use', 'AUDIO SCK')), g('PC11')),
    (pin('PA14', 'dbg', ('note', 'SWCLK')), g('PA15', ('tim', 'TIM2_CH1'))),
    (b('PA10', ('use', 'USB ID'), ('com', 'USART1 RX')), pin('PA13', 'dbg', ('note', 'SWDIO'))),
    (g('PA8', ('tim', 'TIM1_CH1'), ('com', 'I2C3 SCL')), b('PA9', ('use', 'USB VBUS'), ('com', 'USART1 TX'))),
    (g('PC8', ('tim', 'TIM3_CH3')), g('PC9', ('tim', 'TIM3_CH4'), ('com', 'I2C3 SDA'))),
    (g('PC6', ('tim', 'TIM3_CH1'), ('com', 'USART6 TX')), b('PC7', ('use', 'AUDIO MCK'), ('com', 'USART6 RX'))),
    (GND, GND),
]

# ---------------------------------------------------------------- F411 Nucleo-64
NUCLEO_CN7 = [
    (g('PC10', ('com', 'SPI3 SCK')), g('PC11', ('com', 'SPI3 MISO'))),
    (g('PC12', ('com', 'SPI3 MOSI')), g('PD2')),
    (pw('VDD'), pw('E5V')),
    (pin('BOOT0', 'dbg'), GND),
    (NC, NC),
    (NC, pw('IOREF')),
    (pin('PA13', 'dbg', ('note', 'SWDIO')), pin('RESET', 'dbg', ('note', 'NRST'))),
    (pin('PA14', 'dbg', ('note', 'SWCLK')), pw('+3V3')),
    (g('PA15', ('tim', 'TIM2_CH1')), pw('+5V')),
    (GND, GND),
    (g('PB7', ('com', 'I2C1 SDA'), ('tim', 'TIM4_CH2')), GND),
    (b('PC13', ('use', 'USER BTN B1')), pw('VIN')),
    (pin('PC14', 'nc', ('note', '32 kHz XTAL')), NC),
    (pin('PC15', 'nc', ('note', '32 kHz XTAL')), g('PA0', ('ard', 'A0'), ('adc', 'ADC IN0'))),
    (pin('PH0', 'nc', ('note', '8 MHz MCO')), g('PA1', ('ard', 'A1'), ('adc', 'ADC IN1'))),
    (pin('PH1', 'nc', ('note', 'OSC OUT')), g('PA4', ('ard', 'A2'), ('adc', 'ADC IN4'))),
    (pw('VBAT'), g('PB0', ('ard', 'A3'), ('adc', 'ADC IN8'))),
    (g('PC2', ('adc', 'ADC IN12')), g('PC1', ('ard', 'A4'), ('adc', 'ADC IN11'))),
    (g('PC3', ('adc', 'ADC IN13')), g('PC0', ('ard', 'A5'), ('adc', 'ADC IN10'))),
]

NUCLEO_CN10 = [
    (g('PC9', ('tim', 'TIM3_CH4'), ('com', 'I2C3 SDA')), g('PC8', ('tim', 'TIM3_CH3'))),
    (g('PB8', ('ard', 'D15'), ('tim', 'TIM4_CH3')), g('PC6', ('tim', 'TIM3_CH1'), ('com', 'USART6 TX'))),
    (g('PB9', ('ard', 'D14'), ('tim', 'TIM4_CH4')), g('PC5', ('adc', 'ADC IN15'))),
    (pw('AVDD'), pw('U5V')),
    (GND, NC),
    (b('PA5', ('use', 'LED LD2'), ('ard', 'D13')), g('PA12', ('com', 'USB DP'))),
    (g('PA6', ('ard', 'D12'), ('adc', 'ADC IN6')), g('PA11', ('com', 'USB DM'), ('tim', 'TIM1_CH4'))),
    (g('PA7', ('ard', 'D11'), ('adc', 'ADC IN7')), g('PB12')),
    (g('PB6', ('ard', 'D10'), ('com', 'I2C1 SCL')), NC),
    (g('PC7', ('ard', 'D9'), ('tim', 'TIM3_CH2')), GND),
    (g('PA9', ('ard', 'D8'), ('com', 'USART1 TX')), pin('PB2', 'nc', ('note', 'BOOT1'))),
    (g('PA8', ('ard', 'D7'), ('tim', 'TIM1_CH1')), g('PB1', ('adc', 'ADC IN9'), ('tim', 'TIM3_CH4'))),
    (g('PB10', ('ard', 'D6'), ('tim', 'TIM2_CH3')), g('PB15', ('com', 'SPI2 MOSI'))),
    (g('PB4', ('ard', 'D5'), ('tim', 'TIM3_CH1')), g('PB14', ('com', 'SPI2 MISO'))),
    (g('PB5', ('ard', 'D4'), ('tim', 'TIM3_CH2')), g('PB13', ('com', 'SPI2 SCK'))),
    (pin('PB3', 'dbg', ('ard', 'D3'), ('note', 'SWO')), GND),
    (g('PA10', ('ard', 'D2'), ('com', 'USART1 RX')), g('PC4', ('adc', 'ADC IN14'))),
    (pin('PA2', 'nc', ('ard', 'D1'), ('note', 'ST-LINK VCP TX')), NC),
    (pin('PA3', 'nc', ('ard', 'D0'), ('note', 'ST-LINK VCP RX')), NC),
]

FONT = "ui-monospace, 'SFMono-Regular', Menlo, Consolas, 'Liberation Mono', monospace"
ROW = 32
TOP = 200
NAME_W = 62
CH = 7.3  # approx char width at 12px mono
W = 2000

out = []

def add(s):
    out.append(s)

def tag_w(label):
    return round(len(label) * CH + 16)

def pill(x, y, w, h, fill, stroke=None, r=None, dash=None):
    r = h / 2 if r is None else r
    s = f' stroke="{stroke}" stroke-width="1.5"' if stroke else ''
    if dash:
        s += f' stroke-dasharray="{dash}"'
    add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="{r}" fill="{fill}"{s}/>')

def text(x, y, s, size=12, fill='#1f2328', anchor='middle', weight='600'):
    add(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" dominant-baseline="central">{escape(s)}</text>')

def name_pill(cx, cy, p):
    name, cat, _ = p
    fill, fg = CAT[cat]
    pill(cx - NAME_W / 2, cy - 11, NAME_W, 22, fill)
    text(cx, cy, name, 13, fg, weight='700')

def tags(x, cy, p, direction):
    """Draw a pin's tags starting at x, going left (-1) or right (+1)."""
    for kind, label in p[2]:
        w = tag_w(label)
        fill, stroke, fg = TAG[kind]
        left = x - w if direction < 0 else x
        pill(left, cy - 10, w, 20, fill, stroke, r=4)
        text(left + w / 2, cy, label, 11.5, fg)
        x += direction * (w + 6)

def header(cx, rows, label, mirror=False):
    """A 2xN header drawn at column centre cx. Top view: odd pins in the left column.
    Bottom view (mirror): the board is flipped left-to-right, so even pins are on the left."""
    dx = 13
    n = len(rows)
    y0, y1 = TOP - 18, TOP + (n - 1) * ROW + 18
    pill(cx - 2 * dx, y0, 4 * dx, y1 - y0, '#2b2f36', r=6)
    text(cx, y0 - 34, label, 18, '#1f2328', weight='800')
    text(cx, y0 - 15, 'even | odd' if mirror else 'odd | even', 11, '#6b7178', weight='600')
    for i, (odd, even) in enumerate(rows):
        cy = TOP + i * ROW
        left, right = (even, odd) if mirror else (odd, even)
        nl, nr = (2 * i + 2, 2 * i + 1) if mirror else (2 * i + 1, 2 * i + 2)
        for x, num in ((cx - dx, nl), (cx + dx, nr)):
            if num == 1:  # pin 1 is the square pad
                add(f'<rect x="{x - 7:.1f}" y="{cy - 7:.1f}" width="14" height="14" fill="#d9a400"/>')
            else:
                add(f'<circle cx="{x:.1f}" cy="{cy}" r="6.5" fill="#d9a400"/>')
            text(x, cy, str(num), 7.5, '#2b2f36', weight='800')
        lx = cx - 2 * dx - 10 - NAME_W / 2
        rx = cx + 2 * dx + 10 + NAME_W / 2
        name_pill(lx, cy, left)
        name_pill(rx, cy, right)
        tags(lx - NAME_W / 2 - 6, cy, left, -1)
        tags(rx + NAME_W / 2 + 6, cy, right, +1)

# ---------------------------------------------------------------- board sketches
def sketch_frame(bx, by, bw, bh, view, left_name, right_name, usb_top, usb_bottom):
    dash = '8 6' if view == 'bottom' else None
    pill(bx, by, bw, bh, '#e8eef5', '#9fb3c8', r=18, dash=dash)
    text(bx + bw / 2, by - 18, f'board, {view} view', 13, '#4b5158')
    pill(bx + bw / 2 - 34, by - 6, 68, 40, '#9aa4ae' if view == 'top' else '#c3c7cc', r=4)
    text(bx + bw / 2, by + 52, usb_top, 12, '#1f2328')
    for x in (bx + 16, bx + bw - 40):
        pill(x, by + 30, 24, bh - 60, '#2b2f36', r=4)
    add(f'<rect x="{bx + 20}" y="{by + 36}" width="8" height="8" fill="#d9a400"/>')
    add(f'<rect x="{bx + bw - 36}" y="{by + 36}" width="8" height="8" fill="#d9a400"/>')
    text(bx + 28, by + 22, left_name, 12, '#1f2328', weight='800')
    text(bx + bw - 28, by + 22, right_name, 12, '#1f2328', weight='800')
    if usb_bottom:
        pill(bx + bw / 2 - 24, by + bh - 26, 48, 32, '#9aa4ae' if view == 'top' else '#c3c7cc', r=4)
        text(bx + bw / 2, by + bh - 44, usb_bottom, 11, '#1f2328')

def bottom_note(bx, by, bw, left_name, right_name, other_side):
    lines = ['Flipped left-to-right:', f'{left_name} is now on the left,', f'{right_name} on the right, and',
             'even pins are in the', 'left column.', '', 'Pin 1 is still the', 'square pad at the', 'ST-LINK end.',
             '', other_side[0], other_side[1], 'other side.']
    for i, s in enumerate(lines):
        text(bx + bw / 2, by + 200 + i * 24, s, 13, '#4b5158')

def disco_sketch(view, bx, by, bw, bh):
    if view == 'bottom':
        sketch_frame(bx, by, bw, bh, view, 'P2', 'P1', 'ST-LINK USB end', 'USB OTG end')
        bottom_note(bx, by, bw, 'P2', 'P1', ('LEDs, buttons and the', 'MCU are on the'))
        return
    sketch_frame(bx, by, bw, bh, view, 'P1', 'P2', 'ST-LINK USB (mini-B)', 'USB OTG (micro-B)')
    pill(bx + 60, by + 80, bw - 120, 70, '#d3dde8', '#9fb3c8', r=6)
    text(bx + bw / 2, by + 115, 'ST-LINK/V2 debugger', 12, '#4b5158')
    pill(bx + bw / 2 - 70, by + 200, 140, 140, '#2b2f36', r=6)
    text(bx + bw / 2, by + 260, 'STM32', 15, '#ffffff', weight='800')
    text(bx + bw / 2, by + 282, 'F407VGT6', 12, '#c3c7cc')
    lx, ly = bx + bw / 2, by + 450
    pill(lx - 16, ly - 16, 32, 32, '#4b5158', r=3)
    text(lx + 30, ly + 30, 'accel', 10, '#4b5158', anchor='start')
    for dx, dy, col, lbl in ((0, -44, '#f08c00', 'LD3 PD13'), (-44, 0, '#2e9d4b', 'LD4 PD12'),
                             (44, 0, '#d93025', 'LD5 PD14'), (0, 60, '#1a73e8', 'LD6 PD15')):
        add(f'<circle cx="{lx + dx}" cy="{ly + dy}" r="9" fill="{col}"/>')
        ax = 'middle' if dx == 0 else ('end' if dx < 0 else 'start')
        tx = lx + dx + (0 if dx == 0 else (-14 if dx < 0 else 14))
        ty = ly + dy + (-18 if dy < 0 else (18 if dy > 0 else 0))
        text(tx, ty, lbl, 10.5, '#1f2328', anchor=ax)
    for x, col, lbl in ((bx + 95, '#1a73e8', 'B1 USER · PA0'), (bx + bw - 95, '#1f2328', 'B2 RESET')):
        add(f'<circle cx="{x}" cy="{by + 575}" r="17" fill="{col}"/>')
        text(x, by + 607, lbl, 11, '#1f2328')

def nucleo_sketch(view, bx, by, bw, bh):
    if view == 'bottom':
        sketch_frame(bx, by, bw, bh, view, 'CN10', 'CN7', 'ST-LINK USB end', None)
        bottom_note(bx, by, bw, 'CN10', 'CN7', ('LED, buttons, MCU and the', 'Arduino headers are on the'))
        return
    sketch_frame(bx, by, bw, bh, view, 'CN7', 'CN10', 'ST-LINK USB (mini-B)', None)
    pill(bx + 60, by + 80, bw - 120, 70, '#d3dde8', '#9fb3c8', r=6)
    text(bx + bw / 2, by + 115, 'ST-LINK/V2-1 debugger', 12, '#4b5158')
    text(bx + bw / 2, by + 165, 'cut here to separate', 10, '#6b7178')
    add(f'<line x1="{bx + 44}" y1="{by + 178}" x2="{bx + bw - 44}" y2="{by + 178}" stroke="#9fb3c8" stroke-width="2" stroke-dasharray="6 5"/>')
    # Arduino headers just inside the morpho headers
    for x, top_lbl, bot_lbl, y_a, h_a, y_b, h_b in (
            (bx + 48, ('CN6', 'power'), ('CN8', 'A0–A5'), by + 250, 120, by + 395, 105),
            (bx + bw - 66, ('CN5', 'D8–D15'), ('CN9', 'D0–D7'), by + 210, 165, by + 395, 140)):
        pill(x, y_a, 18, h_a, '#4b5158', r=3)
        pill(x, y_b, 18, h_b, '#4b5158', r=3)
        anchor = 'start' if x < bx + bw / 2 else 'end'
        tx = x + 26 if anchor == 'start' else x - 8
        for (y, h), lbl in (((y_a, h_a), top_lbl), ((y_b, h_b), bot_lbl)):
            text(tx, y + h / 2 - 8, lbl[0], 10.5, '#1f2328', anchor=anchor, weight='800')
            text(tx, y + h / 2 + 8, lbl[1], 10.5, '#1f2328', anchor=anchor)
    pill(bx + bw / 2 - 45, by + 310, 90, 90, '#2b2f36', r=6)
    text(bx + bw / 2, by + 345, 'STM32', 13, '#ffffff', weight='800')
    text(bx + bw / 2, by + 365, 'F411RET6', 10.5, '#c3c7cc')
    add(f'<circle cx="{bx + bw - 120}" cy="{by + 255}" r="8" fill="#2e9d4b"/>')
    text(bx + bw - 134, by + 255, 'LD2 PA5', 10.5, '#1f2328', anchor='end')
    for x, col, lbl in ((bx + 120, '#1a73e8', 'B1 USER · PC13'), (bx + bw - 120, '#1f2328', 'B2 RESET')):
        add(f'<circle cx="{x}" cy="{by + 200}" r="14" fill="{col}"/>')
        text(x, by + 226, lbl, 10.5, '#1f2328')

# ---------------------------------------------------------------- boards
BOARDS = {
    'f407-discovery': dict(
        title='STM32F4DISCOVERY', subtitle='STM32F407VG · MB997',
        left=('P1', DISCO_P1), right=('P2', DISCO_P2), sketch=disco_sketch,
        notes=[
            'Pin 1 is the square pad, at the ST-LINK end. Pin names are also printed on the board.',
            'PH0/PH1 and PC14/PC15 reach the headers only if solder bridges SB13/14, SB15/16 are closed.',
            'GPIOs are 3.3 V. Most are 5 V tolerant as inputs (not the ADC pins). Max 25 mA per pin.',
        ],
        source='Source: ST UM1472 (STM32F4DISCOVERY user manual), Table 5. Drawn for ENCS4101, Birzeit University.'),
    'f411-nucleo': dict(
        title='NUCLEO-F411RE', subtitle='STM32F411RE · MB1136 · ST morpho headers',
        left=('CN7', NUCLEO_CN7), right=('CN10', NUCLEO_CN10), sketch=nucleo_sketch,
        notes=[
            'Pin 1 is the square pad, at the ST-LINK end. Blue tags are the Arduino header names.',
            'PA2/PA3 (D1/D0) carry the ST-LINK virtual COM port and are off the headers by default (SB62/63 open).',
            'PH0 takes the 8 MHz MCO clock from the ST-LINK; PC14/PC15 drive the 32 kHz crystal (board C-02 or later).',
            'GPIOs are 3.3 V. Most are 5 V tolerant as inputs (not the ADC pins). Max 25 mA per pin.',
        ],
        source='Source: ST UM1724 (STM32 Nucleo-64 user manual), Tables 16 and 29. Drawn for ENCS4101, Birzeit University.'),
}

VIEWS = {'top': 'top view (component side)', 'bottom': 'bottom view (solder side)'}

def draw(board, view):
    out.clear()
    rows = max(len(board['left'][1]), len(board['right'][1]))
    bh = (rows - 1) * ROW + 60  # board sketch height follows the header length
    legend_y = TOP + rows * ROW + 80
    notes = board['notes']
    H = legend_y + 150 + len(notes) * 30 + 60
    add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
    add(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
    text(60, 62, board['title'], 34, '#1f2328', anchor='start', weight='800')
    text(60, 98, f"{board['subtitle']} · header pinout, {VIEWS[view]}", 16, '#4b5158', anchor='start')
    text(W - 60, 62, 'ENCS4101', 22, '#0369a1', anchor='end', weight='800')
    text(W - 60, 92, 'encs4101.birzeit.me/setup/pinout', 13, '#4b5158', anchor='end')

    (ln, lrows), (rn, rrows) = board['left'], board['right']
    if view == 'top':
        header(520, lrows, f'{ln} (left edge)')
        header(1480, rrows, f'{rn} (right edge)')
    else:
        header(520, rrows, f'{rn} (left edge from below)', mirror=True)
        header(1480, lrows, f'{ln} (right edge from below)', mirror=True)
    board['sketch'](view, 820, TOP + 30, 360, bh - 30)

    # Legend
    add(f'<rect x="0" y="{legend_y - 40}" width="{W}" height="{H - legend_y + 40}" fill="#f3f5f7"/>')
    items = [('gnd', 'Ground'), ('pwr', 'Power'), ('free', 'Free GPIO'),
             ('board', 'GPIO wired on the board'), ('dbg', 'Debug / boot'), ('nc', 'Not usable by default')]
    for i, (cat, lbl) in enumerate(items):
        x, y = 60 + (i // 3) * 330, legend_y + (i % 3) * 38
        pill(x, y - 11, 46, 22, CAT[cat][0])
        text(x + 62, y, lbl, 15, '#1f2328', anchor='start')
    tagitems = [('use', 'ON-BOARD', 'What the board wires it to'), ('adc', 'ADC IN4', 'ADC1 channel'),
                ('tim', 'TIM4_CH4', 'Timer channel'), ('com', 'I2C1 SCL', 'I2C / SPI / USART')]
    if board['title'].startswith('NUCLEO'):
        tagitems.append(('ard', 'D14', 'Arduino header name'))
    for i, (kind, sample, lbl) in enumerate(tagitems):
        x, y = 740 + (i // 2) * 360, legend_y + (i % 2) * 38
        fill, stroke, fg = TAG[kind]
        w = tag_w(sample)
        pill(x, y - 10, w, 20, fill, stroke, r=4)
        text(x + w / 2, y, sample, 11.5, fg)
        text(x + w + 14, y, lbl, 15, '#1f2328', anchor='start')
    text(740, legend_y + 92, 'Never reuse PA13 / PA14 (SWD): the debugger can no longer connect.', 14, '#c62828', anchor='start', weight='700')
    for i, s in enumerate(notes):
        text(740, legend_y + 122 + i * 30, s, 14, '#1f2328', anchor='start')
    text(60, H - 34, board['source'], 12, '#6b7178', anchor='start', weight='500')
    add('</svg>')
    return '\n'.join(out)

for key, board in BOARDS.items():
    for view in VIEWS:
        path = f'{OUT_DIR}/{key}-{view}.svg'
        open(path, 'w').write(draw(board, view))
        print('wrote', path)

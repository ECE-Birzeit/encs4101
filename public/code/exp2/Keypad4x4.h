#ifndef KEYPAD4X4_H
#define KEYPAD4X4_H

#include "main.h"

/* Which column reads high. NO_COLUMN when no key in the driven row is down. */
typedef enum
{
    NO_COLUMN = 0,
    COL1,
    COL2,
    COL3,
    COL4
} ColumnInput;

void        drive_row_high(uint8_t row);                   /* row 0-3 high, the others low */
ColumnInput read_columns(void);                            /* first column that reads high */
uint8_t     decode_key(uint8_t row, ColumnInput column);   /* row + column -> character    */

#endif /* KEYPAD4X4_H */

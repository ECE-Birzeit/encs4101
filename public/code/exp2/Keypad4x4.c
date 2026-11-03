#include "Keypad4x4.h"

/* Pin names come from the CubeMX user labels ROW1-ROW4 and COL1-COL4 */
static GPIO_TypeDef *const rowPorts[4] = { ROW1_GPIO_Port, ROW2_GPIO_Port, ROW3_GPIO_Port, ROW4_GPIO_Port };
static const uint16_t      rowPins[4]  = { ROW1_Pin, ROW2_Pin, ROW3_Pin, ROW4_Pin };

static GPIO_TypeDef *const colPorts[4] = { COL1_GPIO_Port, COL2_GPIO_Port, COL3_GPIO_Port, COL4_GPIO_Port };
static const uint16_t      colPins[4]  = { COL1_Pin, COL2_Pin, COL3_Pin, COL4_Pin };

static const uint8_t keymap[4][4] =
{
    { '1', '2', '3', 'A' },
    { '4', '5', '6', 'B' },
    { '7', '8', '9', 'C' },
    { '*', '0', '#', 'D' },
};

void drive_row_high(uint8_t row)
{
    for (uint8_t i = 0; i < 4; i++)
    {
        HAL_GPIO_WritePin(rowPorts[i], rowPins[i], (i == row) ? GPIO_PIN_SET : GPIO_PIN_RESET);
    }
}

ColumnInput read_columns(void)
{
    for (uint8_t i = 0; i < 4; i++)
    {
        if (HAL_GPIO_ReadPin(colPorts[i], colPins[i]) == GPIO_PIN_SET)
        {
            return (ColumnInput)(COL1 + i);
        }
    }

    return NO_COLUMN;
}

uint8_t decode_key(uint8_t row, ColumnInput column)
{
    if (row > 3 || column == NO_COLUMN)
    {
        return 0;
    }

    return keymap[row][column - COL1];
}

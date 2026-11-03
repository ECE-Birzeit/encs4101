#ifndef LCD16X2_I2C_H
#define LCD16X2_I2C_H

#include "main.h"

/* PCF8574 address, already shifted for the HAL (0x27 << 1).
 * Change it if your adapter's A0-A2 jumpers differ. */
#define LCD_I2C_ADDR 0x4E

void LCD_init(void);                           /* Initialise the module before use */
void LCD_displayText(char *text);              /* Display a string from the cursor position */
void LCD_clear(void);                          /* Clear the screen, cursor to row 0, col 0 */
void LCD_setCursor(uint8_t row, uint8_t col);  /* Move the cursor */
void LCD_displayInt(int number);               /* Display an integer as text */

#endif /* LCD16X2_I2C_H */

/* USER CODE BEGIN 4 */
/* Takes one key of the PIN. Returns 1 once the correct PIN is complete. */
uint8_t password_check(uint8_t key)
{
    static int  count = 0;              /* digits entered so far */
    static char input[PASSWORD_LENGTH];

    input[count] = key;

    LCD_setCursor(1, count);
    LCD_displayText("*");               /* never echo the PIN itself */

    count++;

    if (count < PASSWORD_LENGTH)
    {
        return 0;                       /* wait for the next digit */
    }

    count = 0;                          /* the next attempt starts over */

    if (strncmp(input, PASSWORD, PASSWORD_LENGTH) == 0)
    {
        LCD_clear();
        LCD_setCursor(0, 0);
        LCD_displayText("Correct PIN");
        return 1;                       /* unlocked */
    }

    LCD_clear();
    LCD_setCursor(0, 0);
    LCD_displayText("Try again: ");
    return 0;
}

void handle_keypress(uint8_t key)
{
    char numStr[16];

    LCD_clear();
    LCD_setCursor(0, 0);
    sprintf(numStr, "%c", key);
    LCD_displayText(numStr);
}
/* USER CODE END 4 */

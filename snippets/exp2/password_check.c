/* USER CODE BEGIN 4 */
void password_check(void)
{
    int  pos = -1;
    char input[PASSWORD_LENGTH];

    while (1)
    {
        if (pressFlag == 1)
        {
            pos++;
            input[pos] = key;

            LCD_setCursor(1, pos);
            LCD_displayText("*");       /* never echo the PIN itself */

            pressFlag = 0;
        }

        if (pos >= PASSWORD_LENGTH)
        {
            if (strncmp(input, PASSWORD, PASSWORD_LENGTH) == 0)
            {
                LCD_clear();
                LCD_setCursor(0, 0);
                LCD_displayText("Correct PIN");
                break;                  /* unlocked: carry on */
            }
            else
            {
                LCD_clear();
                LCD_setCursor(0, 0);
                LCD_displayText("Try again: ");
                pos = -1;               /* start the entry over */
            }
        }
    }
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

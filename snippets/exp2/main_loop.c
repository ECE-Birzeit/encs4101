int main(void)
{
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();
    MX_I2C1_Init();

    /* USER CODE BEGIN 2 */
    uint8_t unlocked = 0;      /* 0 until the correct PIN is entered */

    LCD_init();
    LCD_clear();
    LCD_setCursor(0, 0);
    LCD_displayText("Enter Password!");
    /* USER CODE END 2 */

    /* USER CODE BEGIN WHILE */
    while (1)
    {
        if (pressFlag == 1)
        {
            if (!unlocked)
            {
                unlocked = password_check(key);   /* still locked: the key is a PIN digit */
            }
            else
            {
                handle_keypress(key);             /* unlocked: show the key */
            }

            pressFlag = 0;
        }
    }
    /* USER CODE END WHILE */
}

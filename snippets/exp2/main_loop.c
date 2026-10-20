int main(void)
{
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();
    MX_I2C1_Init();

    /* USER CODE BEGIN 2 */
    LCD_init();
    LCD_clear();
    LCD_setCursor(0, 0);
    LCD_displayText("Enter Password!");

    password_check();          /* blocks until the PIN is correct */
    /* USER CODE END 2 */

    /* USER CODE BEGIN WHILE */
    while (1)
    {
        if (pressFlag == 1)
        {
            handle_keypress(key);
            pressFlag = 0;
        }
    }
    /* USER CODE END WHILE */
}

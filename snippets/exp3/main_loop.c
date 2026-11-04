int main(void)
{
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();
    MX_I2C1_Init();
    MX_ADC1_Init();

    /* USER CODE BEGIN 2 */
    LCD_init();
    LCD_clear();
    LCD_setCursor(0, 0);
    LCD_displayText("LAB3 ADC");
    HAL_Delay(1000);
    LCD_clear();
    /* USER CODE END 2 */

    /* USER CODE BEGIN WHILE */
    while (1)
    {
        float vdda = ADC_Get_Vdda();                         /* the real full-scale voltage */

        uint32_t ldr = ADC_Get_Value(&hadc1, ADC_CHANNEL_6); /* PA6: LDR divider */
        uint32_t pot = ADC_Get_Value(&hadc1, ADC_CHANNEL_4); /* PA4: potentiometer */

        LCD_setCursor(0, 0);
        LCD_displayText("LDR:");
        LCD_setCursor(0, 10);
        LCD_displayFloat(ldr * vdda / ADC_FULL_SCALE);
        LCD_displayText("V");

        LCD_setCursor(1, 0);
        LCD_displayText("POT:");
        LCD_setCursor(1, 10);
        LCD_displayFloat(pot * vdda / ADC_FULL_SCALE);
        LCD_displayText("V");

        HAL_Delay(200);
    }
    /* USER CODE END WHILE */
}

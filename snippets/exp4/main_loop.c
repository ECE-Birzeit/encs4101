int main(void)
{
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();
    MX_I2C1_Init();
    MX_ADC1_Init();
    MX_TIM2_Init();
    MX_TIM4_Init();

    /* USER CODE BEGIN 2 */
    LCD_init();
    LCD_clear();
    LCD_setCursor(0, 0);
    LCD_displayText("LAB4 TIMERS");
    HAL_Delay(1000);
    LCD_clear();

    HAL_TIM_Base_Start_IT(&htim2);              /* sample the pot every TIM2 overflow   */
    HAL_TIM_OC_Start(&htim4, TIM_CHANNEL_4);    /* toggle the LED pin on every match     */
    /* USER CODE END 2 */

    /* USER CODE BEGIN WHILE */
    while (1)
    {
        /* New period from the pot. With auto-reload preload on, TIM4 only picks it
           up at its next overflow, so the current LED period is never cut short. */
        __HAL_TIM_SET_AUTORELOAD(&htim4, ConvertADCToARR(&htim4, adcValue));

        outFreq = TIM_Get_Toggle_Freq(&htim4);
        LCD_setCursor(0, 0);
        LCD_displayText("Freq:");
        LCD_setCursor(0, 6);
        LCD_displayFloat(outFreq);
        LCD_displayText(" Hz");

        HAL_Delay(100);
    }
    /* USER CODE END WHILE */
}

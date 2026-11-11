/* USER CODE BEGIN 4 */
/* The clock that actually reaches a timer's prescaler (CK_PSC).
   If the APB prescaler is 1, timers run at PCLK; otherwise the RCC doubles it. */
uint32_t TIM_Get_Clock(TIM_HandleTypeDef *htim)
{
    if ((uint32_t)htim->Instance >= APB2PERIPH_BASE)   /* TIM1, TIM8, TIM9-11 */
    {
        uint32_t pclk2 = HAL_RCC_GetPCLK2Freq();
        return ((RCC->CFGR & RCC_CFGR_PPRE2) == RCC_CFGR_PPRE2_DIV1) ? pclk2 : 2 * pclk2;
    }
    uint32_t pclk1 = HAL_RCC_GetPCLK1Freq();           /* TIM2-TIM5, TIM6-7, TIM12-14 */
    return ((RCC->CFGR & RCC_CFGR_PPRE1) == RCC_CFGR_PPRE1_DIV1) ? pclk1 : 2 * pclk1;
}

/* Map a 12-bit ADC reading (0-4095) to the ARR that gives MIN_FREQ_HZ..MAX_FREQ_HZ
   on a toggle-on-match output. The pin toggles once per overflow, so one LED period
   takes two overflows: the timer has to overflow at twice the LED frequency. */
uint32_t ConvertADCToARR(TIM_HandleTypeDef *htim, uint32_t adc_value)
{
    float freq      = MIN_FREQ_HZ + (MAX_FREQ_HZ - MIN_FREQ_HZ) * adc_value / 4095.0f;
    uint32_t psc    = htim->Instance->PSC;
    uint32_t tim_clk = TIM_Get_Clock(htim);

    return (uint32_t)(tim_clk / ((psc + 1) * 2.0f * freq)) - 1;
}

/* Read PSC and ARR back from the timer and work out the frequency it is really
   producing: timer period = (PSC + 1)(ARR + 1) / clock, LED period = 2 x timer period. */
float TIM_Get_Toggle_Freq(TIM_HandleTypeDef *htim)
{
    uint32_t psc = htim->Instance->PSC;
    uint32_t arr = htim->Instance->ARR;
    float period = (float)(psc + 1) * (arr + 1) / TIM_Get_Clock(htim);

    return 1.0f / (2.0f * period);
}

/* Single channel, single conversion, as in Experiment 3. */
uint32_t ADC_Get_Value(ADC_HandleTypeDef *hadc, uint32_t channel)
{
    ADC_ChannelConfTypeDef sConfig = {0};
    uint32_t value = 0;

    sConfig.Channel      = channel;
    sConfig.Rank         = 1;
    sConfig.SamplingTime = ADC_SAMPLETIME_144CYCLES;
    if (HAL_ADC_ConfigChannel(hadc, &sConfig) != HAL_OK)
    {
        Error_Handler();
    }

    HAL_ADC_Start(hadc);
    if (HAL_ADC_PollForConversion(hadc, 100) == HAL_OK)
    {
        value = HAL_ADC_GetValue(hadc);
    }
    HAL_ADC_Stop(hadc);

    return value;
}

/* Show a float with 2 decimals, padded to 6 characters so a shorter number
   overwrites a longer one cleanly ("  1.00" after "100.00"). */
void LCD_displayFloat(float value)
{
    char text[12];
    snprintf(text, sizeof text, "%6.2f", value);
    LCD_displayText(text);
}
/* USER CODE END 4 */

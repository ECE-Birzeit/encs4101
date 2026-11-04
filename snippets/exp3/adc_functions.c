/* USER CODE BEGIN 4 */
/* Point ADC1 at one channel and convert it once (single channel, single conversion). */
uint32_t ADC_Get_Value(ADC_HandleTypeDef *hadc, uint32_t channel)
{
    ADC_ChannelConfTypeDef sConfig = {0};
    uint32_t value = 0;

    sConfig.Channel = channel;
    sConfig.Rank    = 1;
    /* VREFINT must be sampled for at least 10 us (datasheet), so it gets the longest time */
    sConfig.SamplingTime = (channel == ADC_CHANNEL_VREFINT) ? ADC_SAMPLETIME_480CYCLES
                                                             : ADC_SAMPLETIME_144CYCLES;
    if (HAL_ADC_ConfigChannel(hadc, &sConfig) != HAL_OK)
    {
        Error_Handler();
    }

    HAL_ADC_Start(hadc);
    if (HAL_ADC_PollForConversion(hadc, 100) == HAL_OK)   /* wait up to 100 ms */
    {
        value = HAL_ADC_GetValue(hadc);
    }
    HAL_ADC_Stop(hadc);

    return value;
}

/* Measure the real analog supply (VDDA) from the internal reference. */
float ADC_Get_Vdda(void)
{
    uint32_t vrefint     = ADC_Get_Value(&hadc1, ADC_CHANNEL_VREFINT);
    uint16_t vrefint_cal = *VREFINT_CAL_ADDR;

    if (vrefint == 0)
    {
        return VREFINT_CAL_VREF;    /* conversion failed: assume the nominal 3.3 V */
    }
    return VREFINT_CAL_VREF * (float)vrefint_cal / (float)vrefint;
}

/* Show a float with 3 decimals at the cursor, e.g. "1.652". */
void LCD_displayFloat(float value)
{
    char text[12];
    snprintf(text, sizeof text, "%.3f", value);
    LCD_displayText(text);
}
/* USER CODE END 4 */

/* USER CODE BEGIN 4 */
/* Map a 12-bit ADC reading (0-4095) to a compare value for 0-100 % duty.
   In PWM mode 1 the pin is high while CNT < CCR, and CNT runs 0..ARR,
   so CCR = ARR + 1 keeps it high for the whole period (100 %). */
uint32_t ConvertADCToCCR(TIM_HandleTypeDef *htim, uint32_t adc_value)
{
    uint32_t period    = htim->Instance->ARR + 1;     /* counts in one PWM period */
    float    dutyCycle = adc_value / 4095.0f;         /* 0.0 .. 1.0               */

    return (uint32_t)(dutyCycle * period);
}

/* Pick which diagonal of the H-bridge conducts. ENA (the PWM) sets the speed. */
void Motor_SetDirection(MotorDirection dir)
{
    if (dir == CCW)
    {
        HAL_GPIO_WritePin(IN1_GPIO_Port, IN1_Pin, GPIO_PIN_SET);
        HAL_GPIO_WritePin(IN2_GPIO_Port, IN2_Pin, GPIO_PIN_RESET);
    }
    else
    {
        HAL_GPIO_WritePin(IN1_GPIO_Port, IN1_Pin, GPIO_PIN_RESET);
        HAL_GPIO_WritePin(IN2_GPIO_Port, IN2_Pin, GPIO_PIN_SET);
    }
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
/* USER CODE END 4 */

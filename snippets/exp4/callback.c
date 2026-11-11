/* USER CODE BEGIN 4 */
/* Runs every time a timer with its update interrupt enabled overflows.
   Only TIM2 has one here, but check anyway: all timers share this callback. */
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{
    static uint16_t samples[ADC_SAMPLES];   /* the last 4 readings */
    static uint8_t  next;                   /* where the next one goes */

    if (htim->Instance == TIM2)
    {
        samples[next] = ADC_Get_Value(&hadc1, ADC_CHANNEL_4);
        next = (next + 1) % ADC_SAMPLES;

        uint32_t sum = 0;
        for (int i = 0; i < ADC_SAMPLES; i++)
        {
            sum += samples[i];
        }
        adcValue = sum / ADC_SAMPLES;       /* moving average smooths out the noise */
    }
}
/* USER CODE END 4 */

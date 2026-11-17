int main(void)
{
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();
    MX_I2C1_Init();
    MX_ADC1_Init();
    MX_TIM4_Init();

    /* USER CODE BEGIN 2 */
    HAL_TIM_PWM_Start(&htim4, TIM_CHANNEL_4);     /* 20 kHz PWM on ENA, duty 0 for now */
    lastButton = HAL_GPIO_ReadPin(BluePushButton_GPIO_Port, BluePushButton_Pin);
    /* USER CODE END 2 */

    /* USER CODE BEGIN WHILE */
    while (1)
    {
        /* 1. Direction: flip it once per press (polling, with a time-based debounce). */
        GPIO_PinState button = HAL_GPIO_ReadPin(BluePushButton_GPIO_Port, BluePushButton_Pin);
        uint32_t now = HAL_GetTick();

        if (button == BUTTON_PRESSED && lastButton != BUTTON_PRESSED
            && (now - lastPressTick) > DEBOUNCE_MS)
        {
            rotateDir = (rotateDir == CCW) ? CW : CCW;
            lastPressTick = now;
        }
        lastButton = button;
        Motor_SetDirection(rotateDir);

        /* 2. Speed: the potentiometer sets the duty cycle. Below ADC_STOP the motor
              only hums, so switch it off; between ADC_STOP and ADC_START keep the
              last value, so it does not flicker on and off at the threshold. */
        adcValue = ADC_Get_Value(&hadc1, ADC_CHANNEL_4);

        if (adcValue > ADC_START)
        {
            __HAL_TIM_SET_COMPARE(&htim4, TIM_CHANNEL_4, ConvertADCToCCR(&htim4, adcValue));
        }
        else if (adcValue < ADC_STOP)
        {
            __HAL_TIM_SET_COMPARE(&htim4, TIM_CHANNEL_4, 0);
        }

        /* 3. Read the duty cycle back from the timer registers, in %. */
        dutyCycle = (float)TIM4->CCR4 / (TIM4->ARR + 1) * 100;

        HAL_Delay(10);
    }
    /* USER CODE END WHILE */
}

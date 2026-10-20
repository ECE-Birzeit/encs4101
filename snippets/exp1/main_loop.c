int main(void)
{
    /* HAL_Init(), SystemClock_Config() and MX_GPIO_Init() are generated for you */
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();

    /* USER CODE BEGIN WHILE */
    while (1)
    {
        /* The ISR only counts. The main loop does the slow work of
           driving the four LEDs from the current count. */
        WriteBinary4Bit(buttonPressCount);
    }
    /* USER CODE END WHILE */
}

/* USER CODE BEGIN PV */
volatile uint16_t buttonPressCount = 0;

uint32_t currentTick  = 0;
uint32_t previousTick = 0;
const uint32_t debounceTime = 150;   /* ms */
/* USER CODE END PV */

/* USER CODE BEGIN 4 */
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
    if (GPIO_Pin == EXTI_PB_Pin)          /* the pin that raised the interrupt */
    {
        currentTick = HAL_GetTick();      /* ms since reset */

        if ((currentTick - previousTick) > debounceTime)
        {
            buttonPressCount++;
            if (buttonPressCount > 15)    /* 4 bits: wrap 15 -> 0 */
            {
                buttonPressCount = 0;
            }
        }

        previousTick = currentTick;       /* remember this edge */
    }
}
/* USER CODE END 4 */

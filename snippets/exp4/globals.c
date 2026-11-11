/* USER CODE BEGIN Includes */
#include <stdio.h>
#include <LCD16x2_I2C.h>
/* USER CODE END Includes */

/* USER CODE BEGIN PD */
#define MIN_FREQ_HZ   1.0f     /* LED frequency with the potentiometer at 0 V   */
#define MAX_FREQ_HZ   100.0f   /* LED frequency with the potentiometer at 3.3 V */
#define ADC_SAMPLES   4        /* readings averaged by the TIM2 callback        */
/* USER CODE END PD */

/* USER CODE BEGIN PV */
volatile uint16_t adcValue;    /* averaged potentiometer reading, written by the TIM2 callback */
float outFreq;                 /* LED frequency, worked out from TIM4's registers              */
/* USER CODE END PV */

/* USER CODE BEGIN PFP */
uint32_t ADC_Get_Value(ADC_HandleTypeDef *hadc, uint32_t channel);
uint32_t TIM_Get_Clock(TIM_HandleTypeDef *htim);
uint32_t ConvertADCToARR(TIM_HandleTypeDef *htim, uint32_t adc_value);
float    TIM_Get_Toggle_Freq(TIM_HandleTypeDef *htim);
void     LCD_displayFloat(float value);
/* USER CODE END PFP */

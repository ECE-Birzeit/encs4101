/* USER CODE BEGIN Includes */
#include <stdio.h>
#include <LCD16x2_I2C.h>
/* USER CODE END Includes */

/* USER CODE BEGIN PD */
#ifndef VREFINT_CAL_ADDR
#define VREFINT_CAL_ADDR ((uint16_t *)0x1FFF7A2AU) /* factory VREFINT reading, taken at VDDA = 3.3 V */
#endif
#define VREFINT_CAL_VREF 3.3f
#define ADC_FULL_SCALE   4095.0f                    /* 2^12 - 1 for a 12-bit result */
/* USER CODE END PD */

/* USER CODE BEGIN PFP */
uint32_t ADC_Get_Value(ADC_HandleTypeDef *hadc, uint32_t channel);
float    ADC_Get_Vdda(void);
void     LCD_displayFloat(float value);
/* USER CODE END PFP */

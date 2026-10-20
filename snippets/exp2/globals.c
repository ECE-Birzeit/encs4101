/* USER CODE BEGIN Includes */
#include <string.h>
#include <stdio.h>
#include <LCD16x2_I2C.h>
#include <Keypad4x4.h>
/* USER CODE END Includes */

/* USER CODE BEGIN PD */
#define PASSWORD        "1234"   /* predefined PIN */
#define PASSWORD_LENGTH 4
/* USER CODE END PD */

/* USER CODE BEGIN PV */
volatile uint8_t  key          = 0;   /* last decoded key   */
volatile uint8_t  pressFlag    = 0;   /* set by the scanner */
volatile uint8_t  SysTicks     = 0;   /* 1 ms tick counter  */
volatile uint32_t currentTick  = 0;
volatile uint32_t previousTick = 0;

const uint32_t debounceTime = 150;    /* ms */
/* USER CODE END PV */

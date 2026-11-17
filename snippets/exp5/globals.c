/* USER CODE BEGIN PTD */
typedef enum
{
    CCW,    /* counter-clockwise: IN1 = 1, IN2 = 0 */
    CW      /* clockwise:         IN1 = 0, IN2 = 1 */
} MotorDirection;
/* USER CODE END PTD */

/* USER CODE BEGIN PD */
#define ADC_START      900     /* above this reading the motor runs              */
#define ADC_STOP       800     /* below this reading the motor is switched off   */
#define DEBOUNCE_MS    150     /* ignore new presses for this long after one     */

/* The user button reads 1 when pressed on the Discovery (PA0) and 0 on the Nucleo (PC13).
   Keep the line for your board. */
#define BUTTON_PRESSED GPIO_PIN_SET      /* F407 Discovery */
/* #define BUTTON_PRESSED GPIO_PIN_RESET */  /* F411 Nucleo */
/* USER CODE END PD */

/* USER CODE BEGIN PV */
uint16_t       adcValue;              /* potentiometer reading, 0-4095          */
float          dutyCycle;             /* PWM duty cycle in %, read back from TIM4 */
MotorDirection rotateDir = CCW;
GPIO_PinState  lastButton;            /* button level on the previous pass      */
uint32_t       lastPressTick = 0;     /* HAL_GetTick() at the last accepted press */
/* USER CODE END PV */

/* USER CODE BEGIN PFP */
uint32_t ADC_Get_Value(ADC_HandleTypeDef *hadc, uint32_t channel);
uint32_t ConvertADCToCCR(TIM_HandleTypeDef *htim, uint32_t adc_value);
void     Motor_SetDirection(MotorDirection dir);
/* USER CODE END PFP */

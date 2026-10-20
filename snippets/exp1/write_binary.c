/* USER CODE BEGIN 4 */
void WriteBinary4Bit(uint16_t num)
{
    uint16_t bit0, bit1, bit2, bit3;

    bit0 = (num >> 0) & 1;
    bit1 = (num >> 1) & 1;
    bit2 = (num >> 2) & 1;
    bit3 = (num >> 3) & 1;

    HAL_GPIO_WritePin(Bit_0_GPIO_Port, Bit_0_Pin, bit0);
    HAL_GPIO_WritePin(Bit_1_GPIO_Port, Bit_1_Pin, bit1);
    HAL_GPIO_WritePin(Bit_2_GPIO_Port, Bit_2_Pin, bit2);
    HAL_GPIO_WritePin(Bit_3_GPIO_Port, Bit_3_Pin, bit3);
}
/* USER CODE END 4 */

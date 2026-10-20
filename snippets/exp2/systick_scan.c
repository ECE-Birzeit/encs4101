/* USER CODE BEGIN 4 */
void SysTick_Handler(void)
{
    static uint8_t row = 0;

    HAL_IncTick();          /* keep HAL_GetTick() / HAL_Delay() working */
    SysTicks++;

    if (SysTicks == 5)      /* scan one row every 5 ms */
    {
        /* Drive one row high at a time */
        drive_row_high(row);

        /* Read the four column inputs */
        ColumnInput column = read_columns();

        /* A high column means the key at (row, column) is down */
        if ((column == COL1) || (column == COL2) ||
            (column == COL3) || (column == COL4))
        {
            currentTick = HAL_GetTick();

            if ((currentTick - previousTick) > debounceTime)
            {
                key       = decode_key(row, column);
                pressFlag = 1;          /* tell main() there is a key */
            }

            previousTick = currentTick;
        }

        row = (row + 1) % 4;   /* next row on the next scan */
        SysTicks = 0;
    }
}
/* USER CODE END 4 */

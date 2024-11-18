#В матрице найти номер строки, сумма чисел в которой максимальна.
from turtledemo.paint import switchupdown

import numpy as np
import random

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
min_value = int(input("Enter minimum value: "))
max_value = int(input("Enter maximum value: "))

matrix = np.random.randint(min_value,max_value,(rows,cols))

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")
    print()

max_sum = 0
max_row_index = -1

for i, row in enumerate(matrix): #enumerate позволяет перебирать матрицу/списки/etc, возвращая (index, value)
    row_sum = sum(row)
    if row_sum > max_sum:
        max_sum = row_sum
        max_row_index = i

print("Номер строки с максимальной суммой: " , max_row_index+1)
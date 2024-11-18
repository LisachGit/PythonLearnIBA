import random
import sys

A = []
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("incorrect input ")
    sys.exit(1)
for i in range(n):
    a = random.randint(-20, 20)
    A.append(a)
print(A)

#Нахождение суммы отрицательных чисел
sum_negative = sum(x for x in A if x<0)
print("Сумма отрицательных элементов: " , sum_negative)

#Сумма элементов между нулями
try:
    first_zero_index = A.index(0)
    second_zero_index = A.index(0, first_zero_index + 1)
    sum_between = sum(A[first_zero_index + 1 : second_zero_index])
    print("Сумма между двумя первыми нулями: ", sum_between)
except ValueError:
    print("Сумма между двумя первыми нулями: 0")
arr = list(map(float, input("Введите числа через пробел: ").split()))

total = 0
for i in range(len(arr)):
    if i % 2 != 0:
        total += arr[i]

print("Сумма элементов с нечётными индексами:", total)
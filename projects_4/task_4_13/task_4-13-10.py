arr = list(map(float, input("Введите числа через пробел: ").split()))

sum_even = 0
count_even = 0

for i in range(len(arr)):
    if i % 2 == 0:
        sum_even += arr[i]
        count_even += 1

if count_even > 0:
    average = sum_even / count_even
    print("Среднее арифметическое (чётные индексы):", average)
else:
    print("Нет элементов с чётными индексами")
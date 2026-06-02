arr = list(map(float, input("Введите числа через пробел: ").split()))

if len(arr) == 0:
    print("Массив пуст")
else:
    average = sum(arr) / len(arr)
    print("Среднее арифметическое:", average)
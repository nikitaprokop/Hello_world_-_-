arr = list(map(int, input("Введите целые числа через пробел: ").split()))

total = 0
for x in arr:
    if x % 2 != 0:
        total += x

print("Сумма нечётных элементов:", total)
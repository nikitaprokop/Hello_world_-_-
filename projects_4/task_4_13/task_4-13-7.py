arr = list(map(float, input("Введите числа через пробел: ").split()))

count = 0
for x in arr:
    if x > 0:
        count += 1

print("Количество положительных чисел:", count)
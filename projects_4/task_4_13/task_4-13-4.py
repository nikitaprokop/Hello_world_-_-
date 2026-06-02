n = int(input("Сколько чисел будет введено? "))

max_val = float(input("Введите число 1: "))

for i in range(2, n + 1):
    x = float(input(f"Введите число {i}: "))
    if x > max_val:
        max_val = x

print("Максимальное число:", max_val)
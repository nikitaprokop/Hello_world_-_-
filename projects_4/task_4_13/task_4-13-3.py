n = int(input("Введите N: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Сумма первых", n, "натуральных чисел:", total)
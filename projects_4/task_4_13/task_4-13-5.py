n = int(input("Введите N: "))

total = 0
for i in range(1, n + 1):
    total += i * i

print("Сумма квадратов первых", n, "чисел:", total)
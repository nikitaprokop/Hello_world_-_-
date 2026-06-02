n = int(input("Введите N: "))

fact = 1
for i in range(2, n + 1):
    fact *= i

print(f"{n}! = {fact}")
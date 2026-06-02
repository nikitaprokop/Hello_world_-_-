a = [1, 2, 3]
b = [4, 5, 6]

n = len(a)

scalar = 0
i = 0

while i < n:
    scalar = scalar + a[i] * b[i]
    i = i + 1

print("Скалярное произведение двух векторов:", scalar)

array = [7, 3, 8, 1, 4, 6, 2, 5]

print("Исходный массив:", array)

n = len(array)

for i in range(n):
    for j in range(n - 1 - i):
        if array[j] > array[j + 1]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp

print("Отсортированный массив:", array)
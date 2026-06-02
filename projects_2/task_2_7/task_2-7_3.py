pos = input("Последовательность 1 (ATGC):").upper()
pos2 = input("Последовательность 2 (ATGC):").upper()
sequences = pos,pos2

print("Анализ")
print("=" * 40)

for seq in sequences:
    print(f"\nАнализируем последовательность: {seq}")
    print("Её нуклеотиды:")

    for nucleotide in seq:
        print(nucleotide, end=" ")

    print("\n" + "-" * 30)

print("\n" + "=" * 40)
print(" Цикл выполнен")
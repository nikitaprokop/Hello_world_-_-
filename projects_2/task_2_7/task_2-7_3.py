sequences = ["ATATACGCGTA", "CCTCGGNGGA"]

print("Начинаем анализ последовательностей...")
print("=" * 40)

for seq in sequences:
    print(f"\nАнализируем последовательность: {seq}")
    print("Её нуклеотиды (по порядку):")

    for nucleotide in seq:
        print(nucleotide, end=" ")

    print("\n" + "-" * 30)

print("\n" + "=" * 40)

print(" Цикл выполнен!")

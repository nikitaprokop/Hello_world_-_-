files = ["seq1", "seq2", "seq3", "seq4"]

sample_date = "2026-02-23"

print("Обработка файлов:")
print("-" * 30)

for name in files:
    new_name = f"{name}_{sample_date}.fasta"
    print(f"Файл подготовлен: {new_name}")

print("-" * 30)

print("Готово")

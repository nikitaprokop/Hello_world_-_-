files = ["code1", "code2", "code3", "code4"]

sample_date = input("Дата:")

print("Обработка файлов:")
print("-" * 30)

for name in files:
    new_name = f"{name}_{sample_date}.fasta"
    print(f"Файл подготовлен: {new_name}")

print("-" * 30)
print("Готово!")
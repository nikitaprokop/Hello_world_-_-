name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
city = input("Введите ваш город: ")
hobby = input("Введите ваше хобби: ")

file_path = "output.txt"

with open(file_path, 'w', encoding='utf-8') as file:
    file.write("ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ\n")
    file.write("=" * 30 + "\n")
    file.write(f"Имя: {name}\n")
    file.write(f"Возраст: {age}\n")
    file.write(f"Город: {city}\n")
    file.write(f"Хобби: {hobby}\n")
    file.write("=" * 30 + "\n")

print(f"\nИнформация успешно записана в файл {file_path}")

print("\nПроверка содержимого файла:")
print("-" * 30)

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

print("-" * 30)
print("Проверка завершена. Файл содержит указанную выше информацию.")

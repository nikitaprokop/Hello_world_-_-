medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации (°C): ")

with open('recipe.txt', 'w', encoding='utf-8') as file:
    file.write(f"РЕЦЕПТ ПИТАТЕЛЬНОЙ СРЕДЫ\n")
    file.write("=" * 30 + "\n")
    file.write(f"Название: {medium_name}\n")
    file.write(f"Параметры:\n")
    file.write(f"\t- Концентрация агара: {agar_concentration}%\n")
    file.write(f"\t- Температура стерилизации: {sterilization_temp}°C\n")
    file.write("=" * 30 + "\n")

print(f"\nФайл 'recipe.txt' успешно сформирован!")


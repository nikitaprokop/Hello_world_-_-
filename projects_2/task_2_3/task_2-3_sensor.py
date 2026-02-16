operator_name = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение давления (Па): ")

with open('sensor_log.txt', 'w', encoding='utf-8') as file:
    file.write("ЖУРНАЛ ПОКАЗАНИЙ ДАВЛЕНИЯ\n")
    file.write("-" * 30 + "\n")
    file.write("ОПЕРАТОР\tЗНАЧЕНИЕ (Па)\n")
    file.write("-" * 30 + "\n")
    file.write(f"{operator_name}\t{pressure_value}\n")

print(f"\nДанные успешно сохранены в sensor_log.txt")


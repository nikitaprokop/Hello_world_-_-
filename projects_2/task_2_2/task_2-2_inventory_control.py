reagent_name = input("Введите название нового реактива: ")

reagent_quantity = int(input("Введите его количество (целое число): "))

report_message = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."
print(report_message)

with open('inventory.txt', 'w', encoding='utf-8') as file:
    file.write(report_message + "\n")

print("Отчет также сохранен в файл inventory.txt")



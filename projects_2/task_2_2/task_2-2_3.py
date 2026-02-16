
device_name = "Адометр"
inventory_number = "1900-45"
is_operational = True
quantity = 2

print("Название\tИнв. номер\t«исправен»\tКоличество")
print("-" * 50)
print(f"{device_name}\t{inventory_number}\t{is_operational}\t{quantity}")

print("\n" + "=" * 50)
print(f"{'Прибор':<15} {'Инв. №':<12} {'Статус':<10} {'Кол-во':<5}")
print("-" * 50)
print(f"{device_name:<15} {inventory_number:<12} {is_operational!s:<10} {quantity:<5}")



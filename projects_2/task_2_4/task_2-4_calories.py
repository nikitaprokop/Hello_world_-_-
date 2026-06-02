protein = float(input("Введите массу белков (г): "))
fat = float(input("Введите массу жиров (г): "))
carbohydrates = float(input("Введите массу углеводов (г): "))

calories = (protein * 4) + (fat * 9) + (carbohydrates * 4)

print(f"\nОбщая калорийность продукта: {calories:.2f} ккал")
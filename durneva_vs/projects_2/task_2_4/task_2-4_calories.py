proteins = float(input("Введите массу белков (г): "))
fats = float(input("Введите массу жиров (г): "))
carbs = float(input("Введите массу углеводов (г): "))

# Рассчитываем калорийность
calories = (proteins * 4) + (fats * 9) + (carbs * 4)

# Выводим результат
print(f"Общая калорийность продукта: {calories} ккал")
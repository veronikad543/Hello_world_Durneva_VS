weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))

print("--- Отчет о состоянии здоровья ---")
print(f"вес:\t{weight}")
print(f"рост:\t{height}")

bmi = weight / (height ** 2)
print(f"Индекс массы тела пациента: {bmi:.2f}") 
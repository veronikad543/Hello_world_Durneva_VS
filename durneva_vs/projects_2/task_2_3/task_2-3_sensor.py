name_operator = input("Введите имя оператора: ")
current_pressure = input("Введите текущее значение давления (Па): ")
with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f"ОПЕРАТОР: {name_operator}\t ЗНАЧЕНИЕ: {current_pressure}")
print("Данные успешно сохранены в sensor_log.txt")
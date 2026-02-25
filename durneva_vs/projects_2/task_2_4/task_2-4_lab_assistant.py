volume = float(input("Введите объем раствора (мл): "))
salt = volume * 0.009

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-----------------------\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли:  {salt:.2f} г\n")
    file.write(f"Объем воды:  {volume} мл\n")
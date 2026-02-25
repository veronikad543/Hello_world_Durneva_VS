nutrient_medium = input("введите название питательной среды: ")
concentration = input("введите концентрацию агара (%): ")
temperature = input("введите температура стерилизации: ")
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"название питательной среды: {nutrient_medium}\n Параметры\n концентрация агара (%): {concentration}\n температура стерилизации: {temperature}")
    print("Файл 'recipe.txt' успешно сформирован!")
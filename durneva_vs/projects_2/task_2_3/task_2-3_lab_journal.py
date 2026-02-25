researcher = input("Введите ФИО исследователя: ")
date = input("Введите дату: ")
experiment = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("************************************\n")
    file.write("*      ЛАБОРАТОРНЫЙ ЖУРНАЛ         *\n")
    file.write("************************************\n")
    file.write(f"ФИО: {researcher}\n")
    file.write(f"Дата: {date}\n")
    file.write(f"Эксперимент: {experiment}\n")
    file.write(f"Вывод: {conclusion}\n")
    file.write("************************************\n")

print("Страница электронного журнала успешно создана!")

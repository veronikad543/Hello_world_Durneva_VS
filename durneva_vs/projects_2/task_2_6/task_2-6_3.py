donor = input("Введите группу крови донора: ")
patient = input("Введите группу крови пациента: ")

if donor == patient or donor == "O":
    print("Переливание возможно.")
else:
    print("Переливание невозможно.")
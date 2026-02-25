print("=== Анализ последовательности ДНК ===")
dna = input("Введите последовательность ДНК: ").upper()

print("Подсчёт нуклеотидов:")
print(dna.count("A"))
print(dna.count("T"))
print(dna.count("G"))
print(dna.count("C"))

print("Общая длина: ", len(dna))
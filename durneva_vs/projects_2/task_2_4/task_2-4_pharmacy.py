total = int(input("введите общее количество произведенных капсул: "))
capacity = int(input("введите вместимость одной упаковки: "))
complete = total // capacity
remains = total % capacity

print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок: {complete}")
print(f"Остаток капсул: {remains}")
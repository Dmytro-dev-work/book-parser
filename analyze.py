import csv

# Читаємо наш файл із 1000 книжок
with open("books_all.csv", encoding="utf-8-sig") as file:
    rows = list(csv.DictReader(file))

print(f"Всього книжок: {len(rows)}")

# Очищаємо ціну: залишаємо тільки цифри та крапку
for r in rows:
    r["price"] = float("".join(ch for ch in r["Ціна (GBP)"] if ch.isdigit() or ch == "."))
    r["rating"] = int(r["Рейтинг (зірок)"])

# Середня ціна по всьому магазину
avg = sum(r["price"] for r in rows) / len(rows)
print(f"Середня ціна: {avg:.2f} GBP")

# Скільки книжок з максимальним рейтингом
five = [r for r in rows if r["rating"] == 5]
print(f"Книжок із 5 зірками: {len(five)}")

# Найкращі пропозиції (5 зірок і дешево)
deals = sorted([r for r in five if r["price"] < 20], key=lambda r: r["price"])
print(f"\n ТОП-10: круті (5 зірок) і дешеві (< 20 GBP):")
for r in deals[:10]:
    print(f"   {r['price']:>5.2f} GBP — {r['Назва']}")
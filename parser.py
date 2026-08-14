import requests
from bs4 import BeautifulSoup
import csv
import time  # для пауз

# Створюємо CSV-файл із шапкою
with open("books_all.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Назва", "Ціна (GBP)", "Наявність", "Рейтинг (зірок)"])

# Цикл по всіх 50 сторінках
total_books = 0
for page in range(1, 51):  # від 1 до 50
    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"Парсимо сторінку {page}/50...")

    # Завантажуємо сторінку
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    # Знаходимо всі картки книжок
    books = soup.find_all("article", class_="product_pod")

    # Дозаписуємо у файл
    with open("books_all.csv", "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        for book in books:
            # Назва
            title = book.h3.a["title"]

            # Ціна
            price = book.find("p", class_="price_color").text.replace("£", "GBP ")

            # Наявність
            stock = book.find("p", class_="instock availability").text.strip()

            # Рейтинг
            rating_class = book.find("p", class_="star-rating")["class"]
            rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            rating = rating_map.get(rating_class[1], 0)

            writer.writerow([title, price, stock, rating])
            total_books += 1

    
print(f"\nГотово! Зібрано {total_books} книжок у файл books_all.csv")
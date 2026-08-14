# Book Parser & Analyzer

Python-проєкт: парсер збирає 1000 книжок із 50 сторінок сайту
books.toscrape.com, аналізатор знаходить найкращі пропозиції.

## Що вміє
- **parser.py** — збирає назви, ціни, наявність і рейтинг усіх 1000 книжок,
  зберігає у CSV (з паузами, щоб не навантажувати сайт)
- **analyze.py** — аналізує дані: середня ціна, кількість 5-зіркових книжок,
  ТОП-10 «крутих і дешевих» пропозицій
- **books_all.csv** — готовий датасет із 1000 книжок

## Технології
Python 3, requests, BeautifulSoup4, csv

## Як запустити
pip install requests beautifulsoup4
python parser.py
python analyze.py

## Автор
Dmytro — початківець Python-розробник

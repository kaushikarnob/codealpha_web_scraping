
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

base_url = "https://books.toscrape.com/"
all_books = []

for page_number in range(1, 51):

    if page_number == 1:
        url = base_url
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()
        rating = book.find("p", class_="star-rating")["class"][1]

        all_books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    print(f"Page {page_number}: {len(books)} books scraped")

    time.sleep(0.2)

df = pd.DataFrame(all_books)

df.to_csv("books_dataset_final.csv", index=False, encoding="utf-8-sig")

print("\nScraping completed!")
print("Dataset shape:", df.shape)
print("Saved to: books_dataset.csv")
from bs4 import BeautifulSoup as bs4
import requests
import csv

def book_to_csv(books, writer):
    for book in books:
            in_stock = "No"
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            if "In stock" == book.find("p", class_="instock availability").get_text(strip=True):
                in_stock = "Yes"
            writer.writerow([title, price, in_stock])

url="https://books.toscrape.com/catalogue/"

response = requests.get(f"{url}page-1.html")
response.raise_for_status()

soup = bs4(response.content, "html.parser")
books = soup.find_all("article", class_="product_pod")


with open("books.csv", "w",  newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "In Stock?"])

    # write books from the first page
    book_to_csv(books, writer)

    # loop through remaining pages
    while soup.find("li", class_="next"):
        response = requests.get(f"{url}{soup.find("li", class_="next").a["href"]}")
        response.raise_for_status()

        soup = bs4(response.content, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        book_to_csv(books, writer)
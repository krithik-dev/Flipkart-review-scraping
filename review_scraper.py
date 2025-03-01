import requests
from bs4 import BeautifulSoup
import csv

main_url = "https://www.flipkart.com/cmf-nothing-buds-pro-2-50-db-anc-hi-res-ldac-smart-dial-spatial-audio-dual-drivers-bluetooth/product-reviews/itm30c0d780a4c6c?pid=ACCHFZ2FPSFBD9UT&lid=LSTACCHFZ2FPSFBD9UTMQZQP0&marketplace=FLIPKART"

def scrape_positive_reviews(page_num, filename):
    url = f'{main_url}&page={page_num}&sortOrder=POSITIVE_FIRST'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p', class_='z9E0IG')
    stars = soup.find_all(class_='XQDdHH Ga3i8K')
    comments = soup.find_all(class_='ZmyHeo')

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Star', 'Paragraph', 'Comment'])
        for star, paragraph, comment in zip(stars, paragraphs, comments):
            writer.writerow([star.text.strip(), paragraph.text.strip(), comment.text.strip()])

    print(f"Data from page {page_num} for positive reviews has been successfully written to {filename}")


def scrape_negative_reviews(page_num, filename):
    url = f'{main_url}&page={page_num}&sortOrder=NEGATIVE_FIRST'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p', class_='z9E0IG')
    stars = soup.find_all(class_='XQDdHH Js30Fc Ga3i8K')
    comments = soup.find_all(class_='ZmyHeo')

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(['Star', 'Paragraph', 'Comment'])

        for star, paragraph, comment in zip(stars, paragraphs, comments):
            writer.writerow([star.text.strip(), paragraph.text.strip(), comment.text.strip()])

    print(f"Data from page {page_num} for negative reviews has been successfully written to {filename}")


def scrape_positive_pages(num_pages, filename):
    for page_num in range(1, num_pages + 1):
        scrape_positive_reviews(page_num, filename)

def scrape_negative_pages(num_pages, filename):
    for page_num in range(1, num_pages + 1):
        scrape_negative_reviews(page_num, filename)


num_pages_to_scrape = int(input("Enter the number of pages to scrape from the url: "))

print("Scraping positive reviews...")
scrape_positive_pages(num_pages_to_scrape, 'positive_reviews.csv')

print("Scraping negative reviews...")
scrape_negative_pages(num_pages_to_scrape, 'negative_reviews.csv')

print("Scraping complete.")

import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud

main_url = "https://www.flipkart.com/cmf-nothing-buds-pro-2-50-db-anc-hi-res-ldac-smart-dial-spatial-audio-dual-drivers-bluetooth/product-reviews/itm30c0d780a4c6c?pid=ACCHFZ2FPSFBD9UT&lid=LSTACCHFZ2FPSFBD9UTMQZQP0&marketplace=FLIPKART"
stopwords = STOPWORDS

all_positive_comments = ""
all_negative_comments = ""

def scrape_positive_reviews(page_num, filename):
    global all_positive_comments
    
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
            review_text = comment.text.strip()
            all_positive_comments += review_text + " " 
            writer.writerow([star.text.strip(), paragraph.text.strip(), review_text])

    print(f"Data from page {page_num} for positive reviews has been successfully written to {filename}")


def scrape_negative_reviews(page_num, filename):
    global all_negative_comments

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
            review_text = comment.text.strip()
            all_negative_comments += review_text + " "  
            writer.writerow([star.text.strip(), paragraph.text.strip(), review_text])

    print(f"Data from page {page_num} for negative reviews has been successfully written to {filename}")


def scrape_positive_pages(num_pages, filename):
    for page_num in range(1, num_pages + 1):
        scrape_positive_reviews(page_num, filename)


def scrape_negative_pages(num_pages, filename):
    for page_num in range(1, num_pages + 1):
        scrape_negative_reviews(page_num, filename)

def wordcloud_positive():
    wc = WordCloud(background_color="white", stopwords=stopwords, height=700, width=500)
    wc.generate(all_positive_comments)
    wc.to_file("wordcloud_positive.png")

def wordcloud_negative():
    wc = WordCloud(background_color="white", stopwords=stopwords, height=700, width=500)
    wc.generate(all_negative_comments)
    wc.to_file("wordcloud_negative.png")

num_pages_to_scrape = int(input("Enter the number of pages to scrape from the URL: "))

print("Scraping positive reviews...")
scrape_positive_pages(num_pages_to_scrape, 'positive_reviews.csv')

print("Scraping negative reviews...")
scrape_negative_pages(num_pages_to_scrape, 'negative_reviews.csv')

print("\nScraping complete.")

print("Wordcloud created for Positive review")
wordcloud_positive()

print("Wordcloud created for Negative review")
wordcloud_negative()

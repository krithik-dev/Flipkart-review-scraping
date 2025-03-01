# Flipkart-review-scraping

This is a project on scraping user reviews for a perticular product in flipkart india. The program scrape the url of the review section of a perticular project and gives out two csv file with negative reviews and positive review.

### Overall function :

The python program uses requests and BeautifulSoup liberaries
The program srapes flipkart's review page and wirtes in csv file
Reviews are seperated as positive and negative.
The data contains:
> Star rating

> Review title

> Review comment

### Manual changes you might need :
1. The url link must be the "All reviews" page of a perticular product.
2. Make sure the "class-name" or "id" match the page's html script you're trying to scrape.
3. Make sure you have installed all the modules used in program.


> [!NOTE]
> flipkart usually has the same classes and ID on html tags of html. But if the program shows an error, make sure your url has the same class-name and id in the html page.

That is :
```
    paragraphs = soup.find_all('p', class_='z9E0IG')
    stars = soup.find_all(class_='XQDdHH Ga3i8K')
    comments = soup.find_all(class_='ZmyHeo')
```
Here, make sure to check with the class code in the url you have incase if the program failed to sc

> [!NOTE]
> The Required modules are :
    - Requests
    - Bs4 (beautifulSoup)
    - csv
    



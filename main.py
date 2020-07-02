import requests
from bs4 import BeautifulSoup

query = input("Query > ")
price_stripped = []


r = requests.get(f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={query}&_sacat=0") #sends request to EBAY
soup = BeautifulSoup(r.text, 'lxml') #turns response into beautifulsoup obj and sets parser to LXML
prices = soup.find_all("span", {"class": "ITALIC"}) #gets all prices using BS
for price in prices:
    if "$" in price.text and "shipping" not in price.text:
        price = price.text.strip('$')
        price_stripped.append(price)

price_stripped = list(map(float, price_stripped))
try:
    avg = round(round(sum(price_stripped)) / len(price_stripped))
    print(f"Average price for {query} is {avg}")
except ZeroDivisionError:
    print("No Results :(")
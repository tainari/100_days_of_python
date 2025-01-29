import argparse, re, requests
from notification_manager import NotificationManager
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', help="Amazon product URL", required=True)
parser.add_argument('-p','--price', help="Maximum price for alert", required=True, type=float)

args = parser.parse_args()
ITEM_URL = args.url
PRICE_CUTOFF = args.price


HEADERS = {"Accept-Language":"en-US", "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}

response = requests.get(ITEM_URL, headers=HEADERS)
# with open("amazon_switch.txt","w") as f:
#     f.write(response.text)

soup = BeautifulSoup(response.text, "html.parser")
price_outer_container = soup.find_all(name="span", class_="a-price a-text-normal aok-align-center reinventPriceAccordionT2")
price_string = price_outer_container[0].find_next(name="span", class_="a-offscreen").text
price_float = float(price_string.strip().replace("$",""))

item_container = soup.find(name="span", id="productTitle")
item_name = re.sub("\s\s+" , " ", item_container.text)

if price_float < PRICE_CUTOFF:
    message = f"Subject:Deal alert!\n\nThe price of {item_name} is ${price_float:.2f}, below your cutoff of ${PRICE_CUTOFF:.2f}. Buy now! {ITEM_URL}"
    email = NotificationManager(message)

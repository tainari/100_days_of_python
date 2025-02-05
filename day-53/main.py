import os, requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
FORM_URL = os.getenv("FORM_URL")
SCRAPE_URL = "https://appbrewery.github.io/Zillow-Clone/"

# response = requests.get(SCRAPE_URL).text
## For testing purposes
with open("zillow.txt") as f:
    response = f.read()

soup = BeautifulSoup(response, "html.parser")
cards = soup.find_all("div", attrs={"class": "StyledPropertyCardDataWrapper"})
urls = []
addresses = []
prices = []
for card in cards:
    deets = card.find(name="a")
    address = deets.text.strip()
    url = deets.get("href")
    price = card.find(name="span", attrs={"class": "PropertyCardWrapper__StyledPriceLine"}).text.strip().split("+")[0]
    # append to list
    urls.append(url)
    addresses.append(", ".join(address.split(" | ")))
    prices.append(price)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_URL)

for address, price, url in zip(addresses, prices, urls):
    address_element, price_element, url_element = driver.find_elements(By.CLASS_NAME, "Xb9hP")
    # fill address
    address_input = address_element.find_element(By.TAG_NAME, "input")
    address_input.click()
    address_input.send_keys(address)
    # fill price
    price_input = price_element.find_element(By.TAG_NAME, "input")
    price_input.click()
    price_input.send_keys(price)
    # fill url
    url_input = url_element.find_element(By.TAG_NAME, "input")
    url_input.click()
    url_input.send_keys(url)
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    again = driver.find_element(By.LINK_TEXT, "Submit another response")
    again.click()

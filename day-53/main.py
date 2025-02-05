import requests
from bs4 import BeautifulSoup
from selenium import webdriver


URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

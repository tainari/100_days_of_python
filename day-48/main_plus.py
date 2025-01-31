"""
This is the beginning of a Selenium script that automates playing 'regular' Cookie Clicker.
It also opts to buy the cheapest upgrade possible; if none are available, it clicks the cookie.
However, it looks like bots aren't welcome on the main site, so I can't mess around with it more :(
"""

import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

URL = "https://orteil.dashnet.org/cookieclicker/"

def golden_cookie_exists():
    try:
        driver.find_element(By.ID, "goldenCookie")
    except NoSuchElementException:
        return False
    return True

def upgrade_exists():
    try:
        driver.find_element(By.CSS_SELECTOR, ".crate.upgrade.enabled")
    except NoSuchElementException:
        return False
    return True

def building_exists():
    try:
        driver.find_element(By.CSS_SELECTOR, ".product.unlocked.enabled")
    except NoSuchElementException:
        return False
    return True

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

time.sleep(10)

try:
    language = driver.find_element(By.ID, "landSelect-EN").click()
except NoSuchElementException:
    driver.quit()

# Get a connection refused error here *sob*

big_cookie = driver.find_element(By.ID, "bigCookie") # this is bigCookie in the 'real' version

while True:
    # check if an upgrades are available; if so, buy first one
    if upgrade_exists():
        upgrade = driver.find_element(By.CSS_SELECTOR, ".crate.upgrade.enabled")
        upgrade.click()
    # check if anything is available in the store for purchase
    elif building_exists():
        building = driver.find_element(By.CSS_SELECTOR, ".product.unlocked.enabled")
        building.click()
    # otherwise click for cookie
    else:
        big_cookie.click()

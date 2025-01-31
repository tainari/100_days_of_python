"""
This is a Selenium script that automates playing a very basic version of Cookie Clicker.
Quite simply, it opts to buy the cheapest upgrade possible.
If no upgrades are available, it clicks instead.
This is not optimized: lower-level upgrades get less 'valuable' as the game progresses, so at some point,
it's better to skip getting e.g., the cursor and save up for a Factory instead. But that's for later :)
"""


from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By

URL = "https://orteil.dashnet.org/experiments/cookie/"

items = {"buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine", "buyElder Pledge"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)


big_cookie = driver.find_element(By.ID, "cookie")
driver.implicitly_wait(3)

while True:
    store = driver.find_element(By.ID, "store")
    try:
        upgrades = {ug.get_property("id") for ug in driver.find_elements(By.CLASS_NAME, "grayed")}
    except StaleElementReferenceException:
        pass
    else:
        if len(upgrades) == len(items):
            big_cookie.click()
        else:
            upgrade_id = list(items.difference(upgrades))[0]
            try:
                upgrade = driver.find_element(By.ID, upgrade_id).click()
            except StaleElementReferenceException:
                pass
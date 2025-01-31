from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

URL = "https://www.python.org/"
driver.get(URL)

event_div = driver.find_element(By.CSS_SELECTOR, ".medium-widget.event-widget.last")
events = event_div.find_elements(By.TAG_NAME, "li")
event_dict = {}
for ind, event in enumerate(events):
    date, name = event.text.split("\n")
    event_dict[ind] = {'time': date, 'name': name}
print(event_dict)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




URL = "https://secure-retreat-92358.herokuapp.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

## Challenge: LAB Report signup
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("John")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Doe")
email = driver.find_element(By.NAME, "email")
email.send_keys("<EMAIL>")
submit = driver.find_element(By.XPATH, "/html/body/form/button")
submit.click()

## EXPLORING WIKIPEDIA
# URL = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(URL)
# article_count_div = driver.find_element(By.ID, "articlecount")
# article_count = driver.find_elements(By.CSS_SELECTOR, "#articlecount a")[1]
# # article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# # print(article_count.text)
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Forty-seven rōnin")
# all_portals.click()

# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)
# # driver.quit()
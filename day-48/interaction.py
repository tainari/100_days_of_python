from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# article_count_div = driver.find_element(By.ID, "articlecount")
article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(article_count.text)

driver.quit()
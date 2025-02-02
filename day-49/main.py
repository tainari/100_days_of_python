import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

URL = "https://www.linkedin.com/jobs/search/?currentJobId=4128205873&f_AL=true&geoId=103644278&keywords=consultant&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true&sortBy=R"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

# signin_popup = driver.find_element(By.CLASS_NAME, "")
# button = signin_popup.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
# button.click()

signin = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
signin.click()

email = driver.find_element(By.ID, "base-sign-in-modal_session_key")
email.send_keys(EMAIL)
password = driver.find_element(By.ID, "base-sign-in-modal_session_password")
password.send_keys(PASSWORD)
submit_login = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
submit_login.click()

easy_apply_button = driver.find_element(By.XPATH,'//*[@id="ember52"]')
easy_apply_button.click()

easy_apply_phone_number = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
easy_apply_phone_number.send_keys("+14169268676")

easy_apply_submit = driver.find_element(By.XPATH, '//*[@id="ember321"]')
easy_apply_submit.click()

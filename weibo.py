import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def foo(driver):
    driver.get('https://weibo.com/')
    liked = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[text()='赞过的微博']")))
    print(liked.text)
    driver.quit()

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome('chromedriver', options=chrome_options)

try:
    foo(driver)
except Exception as e:
    traceback.print_exc()
    driver.quit()
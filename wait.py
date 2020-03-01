import time, sys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service('IEDriverServer')
service.start()

driver = webdriver.Remote(service.service_url)
driver.get('http://demo.ranzhi.org/')
# driver.implicity_wait(10)
# time.sleep(1) # Let the user actually see something!

name = driver.find_element_by_name('account')
name.clear()
name.send_keys('demo')
# time.sleep(2)

pwd = driver.find_element_by_id('password')
pwd.clear()
pwd.send_keys('qwerpoi')

# time.sleep(2)
btn = driver.find_element_by_id('submit')
btn.click()

#显式等待
try:
    hint = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='bootbox-body']")))
    btn_confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@data-bb-handler='ok']")))
    print(hint.text)
    btn_confirm.click()
except NoSuchElementException as e:
    print(e)
    driver.quit()
    sys.exit()

# time.sleep(2)
pwd.clear()
pwd.send_keys('demo')

time.sleep(1)
btn = driver.find_element_by_id('submit')
btn.click()

time.sleep(5) # Let the user actually see something!
driver.quit()

import time, sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://demo.ranzhi.org/')
time.sleep(3) # Let the user actually see something!

name = driver.find_element_by_name('account')
name.clear()
name.send_keys('demo')
time.sleep(3)

pwd = driver.find_element_by_id('password')
pwd.clear()
pwd.send_keys('qwerpoi')

time.sleep(3)
btn = driver.find_element_by_id('submit')
btn.click()
time.sleep(3)

try:
    hint = driver.find_element_by_xpath("//div[@class='bootbox-body']")
    print(hint.text)
except NoSuchElementException as e:
    print(e)
    driver.quit()
    sys.exit()

btn_confirm = driver.find_element_by_xpath("//button[@data-bb-handler='ok']")
btn_confirm.click()
time.sleep(3)

pwd.clear()
pwd.send_keys('demo')

btn = driver.find_element_by_id('submit')
btn.click()

time.sleep(10) # Let the user actually see something!
driver.quit()
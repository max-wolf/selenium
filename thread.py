from selenium import webdriver
import sys
from time import sleep
from threading import Thread


def test_baidu_search(browser, url):
    driver = None
    # 你可以自定义这里，添加更多浏览器支持进来
    if browser == "ie":
        driver = webdriver.Ie('IEDriverServer')
    elif browser == "chrome":
        driver = webdriver.Chrome('chromedriver')

    if driver == None:
        exit()

    driver.get(url)

    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys(u"开源优测")

    driver.find_element_by_id("su").click()
    sleep(3)

    driver.quit()


if __name__ == "__main__":
    # 浏览器和首页url
    data = {
        "ie": "http://www.baidu.com",
        "chrome": "http://www.baidu.com"
    }

    # 构建线程
    threads = []
    for b, url in data.items():
        t = Thread(target=test_baidu_search, args=(b, url))
        threads.append(t)

        # 启动所有线程
    for thr in threads:
        thr.start()
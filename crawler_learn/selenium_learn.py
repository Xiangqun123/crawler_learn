from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from pyquery import PyQuery as pq
import requests

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_elements_located((By.Id, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()

import time
from bs4 import BeautifulSoup

browser2 = webdriver.Chrome()
browser2.get("https://www.jd.com/")
input = browser2.find_element_by_css_selector('#key')
input.send_keys('iphone')
time.sleep(1)
input.clear()
input.send_keys('ipad')
button = browser2.find_element_by_css_selector('#search > div > div.form > button')
button.click()
htmlindex = BeautifulSoup(browser2.page_source, 'lxml')
a = htmlindex.select('#J_bottomPage > span.p-skip > em:nth-child(1) > b')[0].get_text()
print(a)
i = 1
htmllists = []
# while i <= int(htmlindex('#J_bottomPage > span.p-skip > em:nth-child(1) > b').text()):
#     input2 = browser2.find_element_by_css_selector('#J_bottomPage > span.p-skip > input')
#     htmllists = htmllists.append(browser2.page_source)
#     input2.send_keys('i+1')
#     button2 = browser2.find_element_by_css_selector('#J_bottomPage > span.p-skip > a')
#     button2.click()
#     i += 1

htmlindex = requests.get('https://search.jd.com/Search?keyword=ipad&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=ipad&ev=exbrand_Apple%5E&page=1&click=0').text
soup = BeautifulSoup(htmlindex)
a = soup.select('#J_bottomPage > span.p-skip > em:nth-child(1) > b')[0].get_text()
print(a)
i = 1









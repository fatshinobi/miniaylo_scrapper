import pdb
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from lib.bid import Bid

serv = Service('/usr/bin/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(service=serv, options=chrome_options)

url = 'https://miniaylo.finance.ua/'

driver.get(url)
time.sleep(15)

phone_btns = driver.find_elements(By.XPATH, "//div[@class='phone']/span")

for phone_btn in phone_btns:
    phone_btn.click()

actions = driver.find_elements(By.XPATH, "//tbody[@class='on-data']/tr")

#all_html = driver.page_source

bids_list = []

for action in actions:
    elements = action.find_elements(By.TAG_NAME, 'td')
    if len(elements) < 2: continue

    bids_list.append(Bid(action, driver))
    
for bid in bids_list:
    #pdb.set_trace()
    print(bid)

#pdb.set_trace()

driver.close()

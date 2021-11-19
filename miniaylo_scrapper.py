import pdb
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#chrome_options = Options()
#chrome_options.add_argument('--headless')
serv = Service('/usr/bin/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(service=serv, options=chrome_options)

#from lib.actions_list import ActionsList

url = 'https://miniaylo.finance.ua/'

driver.get(url)
time.sleep(10)
#actions = driver.find_elements_by_class_name('added')

actions = driver.find_elements(By.XPATH, "//tbody[@class='on-data']/tr")

#all_html = driver.page_source

for action in actions:
    action_str = '[ '
    elements = action.find_elements(By.TAG_NAME, 'td')
    for element in elements:
      action_str += f' : {element.text}'

    #for element in action.find_elements(By.TAG_NAME, 'td'):
    #    

    print(f'{action_str} ]')
    #print(action.text)

#pdb.set_trace()

driver.close()

#ActionsList(url)
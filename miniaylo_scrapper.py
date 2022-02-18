import pdb
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#chrome_options = Options()
#chrome_options.add_argument('--headless')
serv = Service('/usr/bin/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(service=serv, options=chrome_options)
#driver = webdriver.Chrome(ChromeDriverManager().install())

#from lib.actions_list import ActionsList

url = 'https://miniaylo.finance.ua/'

driver.get(url)
time.sleep(20)
#actions = driver.find_elements_by_class_name('added')

phone_btns = driver.find_elements(By.XPATH, "//div[@class='phone']/span")

for phone_btn in phone_btns:
    phone_btn.click()

actions = driver.find_elements(By.XPATH, "//tbody[@class='on-data']/tr")

#all_html = driver.page_source


for action in actions:
    hover = ActionChains(driver).move_to_element(action)
    hover.perform()
    
    action_number_string = action.get_attribute('title')

    action_str = '[ '
    action_str += action_number_string
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
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
time.sleep(15)
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
    action_number_parts = action_number_string.split(' ')
    action_number_string = action_number_parts[2] if len(action_number_parts) > 2 else ''

    #action_str = '[ '
    #action_str += action_number_string
    elements = action.find_elements(By.TAG_NAME, 'td')
    
    if len(elements) < 2: continue 

    time_str = elements[0].text
    type_str = elements[1].text
    amount_elem = elements[2]
    amount_childrn = amount_elem.find_elements(By.XPATH, ".//b")
    currency_childrn = amount_elem.find_elements(By.XPATH, ".//span")
    amount_str = amount_childrn[0].text
    currency_str = currency_childrn[0].text

    rate_elem = elements[3]
    rate_childrn = rate_elem.find_elements(By.XPATH, ".//b")
    rate_str = rate_childrn[0].text

    phone_city_note_elem = elements[5]
    phone_elem = phone_city_note_elem.find_elements(By.XPATH, ".//div[@class='group']/div[@class='phone']")
    city_elem = phone_city_note_elem.find_elements(By.XPATH, ".//div[@class='group']/div[@class='city']")
    note_elem = phone_city_note_elem.find_elements(By.XPATH, ".//div[@class='comment']")
    

    phone_str = phone_elem[0].text
    city_str = city_elem[0].text
    note_str = note_elem[0].text

    print(f'[ {action_number_string} : {type_str} : {time_str} : {amount_str} : {currency_str} : {rate_str} : {phone_str} : {city_str} : {note_str} ]')

    #for element in elements:
    #    action_str += f' : {element.text}'

    #for element in action.find_elements(By.TAG_NAME, 'td'):
    #    

    #print(f'{action_str} ]')
    #print(action.text)

#pdb.set_trace()

driver.close()

#ActionsList(url)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class Bid:
    def __init__(self, action_element, driver):
        hover = ActionChains(driver).move_to_element(action_element)
        hover.perform()
        
        action_number_string = action_element.get_attribute('title')
        action_number_parts = action_number_string.split(' ')
        self.action_number = action_number_parts[2] if len(action_number_parts) > 2 else ''

        elements = action_element.find_elements(By.TAG_NAME, 'td')

        self.time_str = elements[0].text
        self.bid_type = elements[1].text
        amount_elem = elements[2]
        amount_childrn = amount_elem.find_elements(By.XPATH, ".//b")
        currency_childrn = amount_elem.find_elements(By.XPATH, ".//span")
        self.amount = amount_childrn[0].text
        self.currency = currency_childrn[0].text

        rate_elem = elements[3]
        rate_childrn = rate_elem.find_elements(By.XPATH, ".//b")
        self.rate = rate_childrn[0].text

        phone_city_note_elem = elements[5]
        phone_elem = phone_city_note_elem.find_elements(By.XPATH, ".//div[@class='group']/div[@class='phone']")
        city_elem = phone_city_note_elem.find_elements(By.XPATH, ".//div[@class='group']/div[@class='city']")
        note_elem = phone_city_note_elem.find_elements(By.XPATH, ".//div[@class='comment']")
        

        self.phone = phone_elem[0].text
        self.city = city_elem[0].text
        self.note = note_elem[0].text

    def __str__(self):
        return f'[ {self.action_number} : {self.bid_type} : {self.time_str} : {self.amount} : {self.currency} : {self.rate} : {self.phone} : {self.city} : {self.note} ]'
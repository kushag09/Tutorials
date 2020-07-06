from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('http://greenworldonline.ml/')

Ltext = driver.find_element_by_link_text('About Us')
Ltext.click()
try:
    elem = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.LINK_TEXT, 'Vision & Mission'))
    )
    elem.click()
    elem.clear()
    
    elem = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.LINK_TEXT, 'The Manure'))
    )
    elem.click()

except:
    driver.quit()

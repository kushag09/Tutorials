from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://techwithtim.net/')
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys('test')
search.send_keys(Keys.RETURN)

cont = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.ID , 'main'))
)

titles = cont.find_elements_by_tag_name("article")
for title in titles:
    vidTitle = title.find_element_by_class_name("entry-summary")
    print(vidTitle.text)

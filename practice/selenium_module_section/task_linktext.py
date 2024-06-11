import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get('https://easysmarthub.ru/blog/')
    
    btn = driver.find_element(By.LINK_TEXT,'Что такое базы данных?')
    
    btn.click()
    time.sleep(3)
    btn2 = driver.find_element(By.LINK_TEXT,'Эрик Спичак')
    btn2.click()
    time.sleep(3)


finally:
    driver.quit()



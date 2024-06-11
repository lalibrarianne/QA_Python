import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/Qa_autotest_01/')
    time.sleep(2)
    input_one = driver.find_element(By.ID,'inputField')

    input_one.send_keys('Erik')
    btn = driver.find_element(By.CSS_SELECTOR,".buttons .btn:nth-child(3)")
 
    btn.click() 
    time.sleep(5) 
 
finally: 
    driver.quit() 



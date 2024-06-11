import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get('https://erikdark.github.io/Qa_autotest_02/')
    
    inputs = driver.find_elements(By.TAG_NAME,'input')
    for i in inputs:
        i.send_keys('text')
    btn = driver.find_element(By.CSS_SELECTOR, '#submitBtn')
    time.sleep(1)
    btn.click()
    time.sleep(3)


finally:
    driver.quit()



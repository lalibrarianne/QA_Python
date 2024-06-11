import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/QA_autotests_09/')
    time.sleep(1)
   
    text_challange = driver.find_element(By.CSS_SELECTOR,'#challenge').text
    nums = re.findall(r'\d+',text_challange)
    print(nums)
    a = int(nums[0])
    b = int(nums[1])
    anser = a+b
    print(anser)
    first_select_container = driver.find_element(By.CSS_SELECTOR,'.container')
    first_select_container.find_element(By.CSS_SELECTOR,'select').click()
    select = Select(driver.find_element(By.TAG_NAME,'select'))
    select.select_by_value(str(anser))



    driver.find_element(By.ID, 'submitBtn').click()
    message = driver.find_element(By.ID,'message').text
    assert 'You guessed it! Well done!' == message
    


finally:
    time.sleep(3)
    driver.quit()


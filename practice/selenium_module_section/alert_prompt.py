import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/QA_autotests_12/')
    time.sleep(1)
    driver.find_element(By.ID,'startTaskBtn').click()
    confirm = driver.switch_to.alert
    confirm.accept()
    time.sleep(2)
    alert = driver.switch_to.alert.text
    nums = re.findall(r'\d+',alert)
    print(nums)
    a = int(nums[0])
    b = int(nums[1])
    anser = a+b
    
    prompt = driver.switch_to.alert
    prompt.send_keys(str(anser))
    time.sleep(2)

    prompt.accept() 
    message = driver.switch_to.alert.text
    
    assert 'Правильно! Ответ 50.' == message
 
finally:
    time.sleep(3)
    driver.quit()


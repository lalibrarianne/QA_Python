import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/Qa_autotest_07/')
    time.sleep(1)
   
    text_challange = driver.find_element(By.CSS_SELECTOR,'#challenge').text
    nums = re.findall(r'\d+',text_challange)
    print(nums)
    a = int(nums[0])
    
    num = driver.find_element(By.ID,'numberImage')
    att = str(num.get_attribute('data-b'))
    att1 = str(re.sub(r'[^\w\s]','', att))
    print(att1)
    b = int(att1[2:])
    
    print (a, b)

    anser = a+b
    print(anser)
    
    driver.find_element(By.ID, 'answer').send_keys(str(anser))
    time.sleep(1)
    driver.find_element(By.ID, 'submitBtn').click()
    text = driver.find_element(By.ID,'message').text
    


finally:
    time.sleep(3)
    driver.quit()


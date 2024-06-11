import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/Qa_autotests_05/')
    time.sleep(2)
    text_challange = driver.find_element(By.CSS_SELECTOR,'#challenge').text
    nums = re.findall(r'\d+',text_challange)
    print(nums)
    b = int(nums[1])
    a = int(nums[0])
    anser = a+b
    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(anser))
    driver.find_element(By.CSS_SELECTOR, '#notRobot').click()
    driver.find_element(By.CSS_SELECTOR, '#cool').click()
    driver.find_element(By.CSS_SELECTOR, '#submitBtn').click()
    text = driver.find_element(By.CSS_SELECTOR,'#message').text
    assert 'Поздравляю, Elon Musk!' == text

finally:
    time.sleep(5)
    driver.quit()


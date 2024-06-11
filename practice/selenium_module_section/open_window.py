import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/QA_autotests_13/')
    time.sleep(1)
    driver.find_element(By.TAG_NAME, 'button').click()
    new_window = driver.window_handles[1]

    driver.switch_to.window(new_window)


    driver.find_element(By.TAG_NAME, 'button').click()
    message = driver.find_element(By.TAG_NAME, 'text').text
    assert 'Я СДЕЛАЛ' == message


finally:
    time.sleep(3)
    driver.quit()


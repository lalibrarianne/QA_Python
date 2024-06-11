import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/Qa_autotest_03/')
    input = driver.find_elements(By.CSS_SELECTOR,'input')
    for i in input:
        i.send_keys('Text@mail.ru')
    btn = driver.find_element(By.CSS_SELECTOR, 'button')
    btn.click()
    time.sleep(1)
    wel_text = driver.find_element(By.CSS_SELECTOR,'h2')
    wel_text_block = wel_text.text


    assert 'Поздравляю, вы прошли первый уровень.' == wel_text_block
   
   


finally:
    time.sleep(5)
    driver.quit()


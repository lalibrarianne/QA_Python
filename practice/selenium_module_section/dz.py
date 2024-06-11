import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/QA_autotest_16/')
    element = driver.find_element(By.CSS_SELECTOR,'#price1')
    condition = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(element,'550'))
    btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'buyButton1'))).click()
    
    
    carPrices = [
    { min: 500, max: 750, step: 50, "выигрышная_цена": 550 }, 
    { min: 750, max: 1500, step: 100, "выигрышная_цена": 800 }, 
    { min: 15000, max: 25000, step: 1000, "выигрышная_цена": 19000 } 
    ]
    inputText = 'Erik'

    inputfield.send_keys(inputText)
    btn.click()

    condition = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#result'),f'Введенный текст: {inputText}'))

    message = driver.find_element(By.ID,'message1')
    assert 'Вы успешно купили автомобиль!' in message.text

finally:
    time.sleep(5)
    driver.quit()

import time
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#@pytest.fixture
#def driver():
   #yield driver
   #driver.quit()

def test_main():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/zachet_selenium_01/')
    driver.find_element(By.LINK_TEXT, 'Регистрация').click()     
    data = ['Friday','friday@example.com','fridaypass123']
    inputs = driver.find_elements(By.TAG_NAME,'input')
    for i in range(len(inputs)):
        inputs[i].send_keys(data[i])
    driver.find_element(By.TAG_NAME,'button').click()

    message = driver.find_element(By.ID,'register-message').text
    assert 'Пользователь зарегистрирован' == message
    
#test_main()

def test_login():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/zachet_selenium_01/')
    driver.find_element(By.LINK_TEXT, 'Логин').click()
    driver.find_element(By.ID,'email').send_keys('fruits@summer.com')
    driver.find_element(By.ID,'password').send_keys('supassfru123')
    driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
    message = driver.find_element(By.ID,'login-message').text
    assert 'Пользователь вошел в систему' == message
    time.sleep(5)

#test_login()

def test_profile():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/zachet_selenium_01/')
    prof = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Профиль'))).click()
    btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'logout-button'))).click()
    message = driver.find_element(By.ID,'logout-message').text
    assert 'Пользователь вышел из системы' == message
    
#test_profile()

def test_sort():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/zachet_selenium_01/')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Таблица данных'))).click()
    #my_dict = {key1:value1, key2:value2, key3:value3}
    text1 = str(driver.find_element(By.ID,'data-table').text)
    print(text1)   
    
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[onclick="sortTable(0)"]'))).click()
    message = driver.find_element(By.ID,'sort-message').text
    assert 'Таблица отсортирована по столбцу 1' == message
    text2 = str(driver.find_element(By.ID,'data-table').text)
    if text2 != text1:
        print('True')
    else:
        print('False')   

    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[onclick="sortTable(1)"]'))).click()
    message = driver.find_element(By.ID,'sort-message').text
    assert 'Таблица отсортирована по столбцу 2' == message
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[onclick="sortTable(2)"]'))).click()
    message = driver.find_element(By.ID,'sort-message').text
    assert 'Таблица отсортирована по столбцу 3' == message

#test_sort()

def test_din():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/zachet_selenium_01/')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Динамический контент'))).click()
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, 'add-element'))).click()
    WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.ID, 'content-area'),"Новый элемент"))
    
    add_msg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//text()[contains(.,'Элемент добавлен')]")))
    
test_din()
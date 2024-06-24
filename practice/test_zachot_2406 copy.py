import time
import pytest
import random
import string
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
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    driver.find_element(By.LINK_TEXT, 'Регистрация').click()     
    name = driver.find_elements(By.ID,'name')
    def generate_false():
        length = random.randint(5,20)
        upp = True
        dig = True
        spec = True

        chars = string.ascii_lowercase
        if upp:
            chars += string.ascii_uppercase
        if dig:
            chars += string.digits
        if spec:
            chars += string.punctuation
    
        gen_name = ''.join(random.choice(chars) for _ in range(length))
        return gen_name

    print(generate_false())

    def generate_true():
        length1 = random.randint(5,20)
        low = True
        upp = True
        
        chars1 = '-'
        if low:
            chars1 += string.ascii_lowercase
        if upp:
            chars1 += string.ascii_uppercase
   
        gen_name1 = ''.join(random.choice(chars1) for _ in range(length1))
        return gen_name1

    print(generate_true())

    try:
        name.send_keys(generate_false())
        print('False')
        name.clear()
        name.send_keys(generate_true())
        print('True')
    except: 
        print ('Ошибка')   
        
    #driver.find_element(By.TAG_NAME,'button').click()

    #message = driver.find_element(By.ID,'register-message').text
    #assert 'Пользователь зарегистрирован' == message
    
test_main()

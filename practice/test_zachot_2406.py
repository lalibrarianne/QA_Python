import time
import pytest
import random
import string
from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

#@pytest.fixture
#def driver():
   #yield driver
   #driver.quit()

def test_main():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Регистрация'))).click() 
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

    email_inp = driver.find_elements(By.ID,'email')
    def valid_e(email):
        if "@" not in email or "." not in email or email.index('@') > email.index('.'):
            return False
        return True
    pass_inp = driver.find_elements(By.ID,'password')
    #def pass_valid(pass_inp):
        #return len(pass_inp)
    #if len(pass_inp)>=8:
        #has_uper = any(char.isupper() for char in p)
        #has_digit = any(char.isdigit() for char in p)
    #if has_uper and has_digit:
        #print('принято')
    #else:
        #print('ошибка')

    pass_conf = driver.find_elements(By.ID,'confirmPassword')    

    #try:
    email_inp.send_keys('noexample.com')
    print('False')
    name.send_keys(generate_false())
    print('False')
    pass_inp.send_keys('newpass')
    print('False')
    pass_conf.send_keys('lololo')
    print('False')
    time.sleep(10)
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click() 
    valid_mes = email_inp.get_property('validationMessage')
    print(f'Valid message{valid_mes}')
    email_inp.clear()
    email_inp.send_keys(valid_e('nololo@example.com'))
    print('True')
    valid_mes = name.get_property('validationMessage')
    print(f'Valid message{valid_mes}')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click() 
    name.clear()
    name.send_keys(generate_true())
    print('True')
    valid_mes = pass_inp.get_property('validationMessage')
    print(f'Valid message{valid_mes}')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click()  
    pass_inp.clear()   
    pass_inp.send_keys('Newpass1')
    print('True')
    valid_mes = pass_conf.get_property('validationMessage')
    print(f'Valid message{valid_mes}')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click()  
    pass_conf.clear()
    pass_conf.send_keys('Newpass1')
    print('True')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click() 


    #except: 
        #print ('Ошибка')   
        
    #message = driver.find_element(By.ID,'message').text
    #assert 'Регистрация успешна!' == message
    
test_main()

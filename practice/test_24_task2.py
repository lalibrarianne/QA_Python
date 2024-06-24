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

@pytest.fixture
def driver():
   yield driver
   driver.quit()

def test_main():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Вход'))).click() 
    login = driver.find_element(By.ID,'login')
    pass_inp = driver.find_element(By.ID,'password')
    login.send_keys('user1')
    pass_inp.send_keys('Pass1234')
    time.sleep(2)
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click() 
    message1 = driver.find_element(By.ID,'loginMessage').text
    assert 'Вход успешен!' == message1
    login.clear()
    pass_inp.clear()
    login.send_keys('user2')
    pass_inp.send_keys('Pass1234')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click() 
    message2 = driver.find_element(By.ID,'loginMessage').text
    assert 'Вход успешен!' == message2
    login.clear()
    pass_inp.clear()
    login.send_keys('user3')
    pass_inp.send_keys('Pass1234')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click() 
    message3 = driver.find_element(By.ID,'loginMessage').text
    assert 'Вход успешен!' == message3
    login.clear()
    pass_inp.clear()
    login.send_keys('user4')
    pass_inp.send_keys('Pass1234')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click() 
    message4 = driver.find_element(By.ID,'loginMessage').text
    assert 'Вход успешен!' == message4
    login.clear()
    pass_inp.clear()
    login.send_keys('user5')
    pass_inp.send_keys('Pass1234')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click() 
    message5 = driver.find_element(By.ID,'loginMessage').text
    assert 'Вход успешен!' == message5
#test_main()

def new_user():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Вход'))).click() 
    new_login = driver.find_element(By.ID,'newLogin').send_keys('Mimi')
    new_pass = driver.find_element(By.ID,'newPassword').send_keys('NewPass24')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//button [text()='Добавить']"))).click()
    
    messagen = driver.find_element(By.ID,'addUserMessage').text
    assert 'Пользователь добавлен!' == messagen

    driver.find_element(By.ID,'login').send_keys('Mimi')
    driver.find_element(By.ID,'password').send_keys('NewPass24')
    
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click() 
    message = driver.find_element(By.ID,'loginMessage').text
    assert 'Вход успешен!' == message

#new_user()

def new_users():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Вход'))).click() 
    driver.find_element(By.ID,'newLogin').send_keys('Kili')
    driver.find_element(By.ID,'newPassword').send_keys('NewPass241')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//button [text()='Добавить']"))).click()
    messagen = driver.find_element(By.ID,'addUserMessage').text
    assert 'Пользователь добавлен!' == messagen
    driver.find_element(By.ID,'newLogin').send_keys('Lili')
    driver.find_element(By.ID,'newPassword').send_keys('NewPass242')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//button [text()='Добавить']"))).click()
    messagen = driver.find_element(By.ID,'addUserMessage').text
    assert 'Пользователь добавлен!' == messagen
    driver.find_element(By.ID,'newLogin').send_keys('Gigi')
    driver.find_element(By.ID,'newPassword').send_keys('NewPass243')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//button [text()='Добавить']"))).click()
    messagen = driver.find_element(By.ID,'addUserMessage').text
    assert 'Пользователь добавлен!' == messagen  
    time.sleep(3)

    login = driver.find_element(By.ID,'login')
    login.send_keys('Kili')
    pass_inp = driver.find_element(By.ID,'password')
    pass_inp.send_keys('NewPass241')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click() 
    message1 = driver.find_element(By.ID,'loginMessage').text
    assert 'Вход успешен!' == message1
    login.clear()
    pass_inp.clear()

    login.send_keys('Lili')
    pass_inp.send_keys('NewPass242')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click() 
    message2 = driver.find_element(By.ID,'loginMessage').text
    assert 'Вход успешен!' == message2
    login.clear()
    pass_inp.clear()

    login.send_keys('Gigi')
    pass_inp.send_keys('NewPass243')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click() 
    message3 = driver.find_element(By.ID,'loginMessage').text
    assert 'Вход успешен!' == message3
    

new_users()


  

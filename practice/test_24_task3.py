import time
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
   yield driver
   driver.quit()

def test_add():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Магазин'))).click() 
    for i in range(3):
        buttons = driver.find_elements(By.CSS_SELECTOR, 'button[class="add-to-cart"]')
        buttons[i].click()
        driver.switch_to.alert.accept()
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'cartButton'))).click() 
    time.sleep(5)
test_add()

def test_double():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Магазин'))).click()
    
    for i in range(3):
        buttons = driver.find_elements(By.CSS_SELECTOR, 'button[class="add-to-cart"]')
        buttons[i].click()
        driver.switch_to.alert.accept()
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-name="Товар 1"]'))).click()
    driver.switch_to.alert.accept()    
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'cartButton'))).click() 

    try:
        cart_e = driver.find_element(By.ID, 'cartItems').text
        assert cart_e.count("Товар 1 - $100") == 2, "Товар 1 не добавлен 2 раза"
        assert cart_e.count("Товар 2 - $200") == 2, "Товар 2 не добавлен 2 раза"
        assert cart_e.count("Товар 3 - $350") == 2, "Товар 3 не добавлен 2 раза"
    except:
        AssertionError
    
test_double()
    
def test_count():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Магазин'))).click() 
    for i in range(3):
        buttons = driver.find_elements(By.CSS_SELECTOR, 'button[class="add-to-cart"]')
        buttons[i].click()
        driver.switch_to.alert.accept()
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'cartButton'))).click() 
    total = 'Общая стоимость: $600'
    cart_t = driver.find_element(By.ID, 'cartTotal').text
    
    if cart_t == total:
        print(True)
    else:
        print(f"Сумма неверна, получилось {cart_t}")
    
test_count()

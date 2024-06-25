from selenium import webdriver  
from selenium.webdriver.common.by import By  
import time  
import pytest  
import re  
  
@pytest.fixture  
def driver():  
    driver = webdriver.Firefox()  
    driver.implicitly_wait(3)  
    yield driver  
    driver.quit()
def test3(driver): 
    driver.get('https://erikdark.github.io/QA_DIPLOM/') 
    driver.find_element(By.CSS_SELECTOR, '[href="shop.html"]').click() 
    for i in range (1,4): 
        btn = driver.find_element(By.CSS_SELECTOR, f'button[data-name="Товар {i}"]').click() 
        driver.switch_to.alert.accept() 
    card = driver.find_element(By.ID, 'cartButton') 
    card.click() 
    cart_e = driver.find_element(By.ID, 'cartItems').text 
    assert "Товар 1 - $100" in cart_e, "Товар 1 не добавлен" 
    assert "Товар 2 - $200" in cart_e, "Товар 2 не добавлен" 
    assert "Товар 3 - $350" in cart_e, "Товар 3 не добавлен" 
    total = 'Общая стоимость: $650' 
    cart_t = driver.find_element(By.ID, 'cartTotal').text 
    assert cart_t == total, f"Сумма неверна, получилос{cart_t}" 
    time.sleep(5)
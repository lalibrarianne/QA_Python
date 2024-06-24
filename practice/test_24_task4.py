import time
import pytest
import pymysql
import pymysql.cursors
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

def test_base():
    driver = webdriver.Chrome()
    driver.get('https://erikdark.github.io/QA_DIPLOM/')
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'База данных'))).click() 
    zapros = driver.find_element(By.ID, 'sqlQuery')
    btn = driver.find_element(By.ID, 'executeButton')
    zapros.send_keys("SELECT * FROM table WHERE name = 'Иван';")
    btn.click()

    zapros.clear()

    zapros.send_keys("ORDER BY age;")
    btn.click()
    message = driver.find_element(By.ID,'sqlMessage').text
    assert 'Данные отсортированы по age.' == message

    zapros.clear()

    zapros.send_keys("DELETE FROM table WHERE id = 1;")
    btn.click()
    
    message = driver.find_element(By.ID,'sqlMessage').text
    assert 'Запись с ID 1 удалена.' == message

    
test_base()
    
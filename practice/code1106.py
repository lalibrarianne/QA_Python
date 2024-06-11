import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def test_main():
    driver = webdriver.Chrome()
    driver.get('http://selenium1py.pythonanywhere.com/ru/')
    driver.find_element(By.LINK_TEXT, 'Предложения').click()
    for i in range(4):
        buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block")
        buttons[i].click()
    driver.find_element(By.XPATH, "//a[contains(@href, '/ru/basket/')]").click()
    driver.find_element(By.LINK_TEXT, 'Перейти к оформлению').click()
    driver.find_element(By.NAME, "username").send_keys("newuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("pass1234567")
    first_select = driver.find_element(By.CLASS_NAME,'radio')
    first_select.find_element(By.ID,'id_options_0').click()
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-block btn-primary"]').click()
    driver.find_element(By.NAME, "first_name").send_keys("Lena")
    driver.find_element(By.NAME, "last_name").send_keys("Lenina")
    driver.find_element(By.NAME, "line1").send_keys("app.4, st.Zelenaya")
    driver.find_element(By.NAME, "line4").send_keys("FlowerCity")
    driver.find_element(By.NAME, "postcode").send_keys("196233")
    select = Select(driver.find_element(By.ID,'id_country'))
    select.select_by_visible_text("Russian Federation")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary"]').click()
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary btn-lg"]').click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary btn-lg btn-block"]').click()

    time.sleep(99)

test_main()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
   driver = webdriver.Chrome()
   yield driver
   driver.quit()


def test_login(driver):
   driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
 
   open_modal_button = WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable((By.ID, 'openModalButton'))
   )
   open_modal_button.click()

   modal = WebDriverWait(driver, 10).until(
       EC.visibility_of_element_located((By.ID, 'loginModal'))
   )
 
   username_field = driver.find_element(By.ID, 'username')
   password_field = driver.find_element(By.ID, 'password')
   login_button = driver.find_element(By.CSS_SELECTOR, '#loginForm button[type="submit"]')

   username_field.send_keys('testuser')
   password_field.send_keys('password123')
   login_button.click()
 
   WebDriverWait(driver, 10).until(
       EC.invisibility_of_element((By.ID, 'loginModal'))
   )
 
   modal_display = driver.execute_script("return document.getElementById('loginModal').style.display")
   assert modal_display == 'none', 'Modal did not close after login'


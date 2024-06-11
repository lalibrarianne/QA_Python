import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import re

driver = webdriver.Chrome()
def test_main():
      
   driver.get('http://selenium1py.pythonanywhere.com/ru/')
   btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT,'Предложения'))).click()
   books_to_add = [
        "Coders at Work",
        "Hacking Exposed Wireless",
        "Visual Guide to Lock Picking",
        "The shellcoder's handbook"
    ]
    
   for book_name in books_to_add:
        book = driver.find_element(By.XPATH, f"//h3/a[contains(text(), '{book_name}')]")
        add_to_cart_button = book.find_element(By.XPATH, "./../../following-sibling::div//button")
        add_to_cart_button.click()

        time.sleep(5)

    #"/ru/basket/add/209/"))).click()

   actions = ActionChains(driver)
   for i in range(4000):
    book = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "/ru/basket/add/209/")))
    actions.click(book)
    actions.perform()
    time.sleep(5)

   book = WebDriverWait(driver,5).until(EC.element_located_to_be_selected(By.LINK_TEXT,("The shellcoder's handbook"))).click()

   book = driver.find_element(By.LINK_TEXT("The shellcoder's handbook"))
   btn = driver.find_element(By.CLASS_NAME,'#btn').click()
   time.sleep(2)
   book2 = driver.find_element(By.PARTIAL_LINK_TEXT("picking_207"))
   btn2 = driver.find_element(By.CLASS_NAME,'#btn').click()
   book3 = driver.find_element(By.PARTIAL_LINK_TEXT("picking_208"))
   btn3 = driver.find_element(By.CLASS_NAME,'#btn').click()
   book4 = driver.find_element(By.PARTIAL_LINK_TEXT("picking_209"))
   btn4 = driver.find_element(By.CLASS_NAME,'#btn').click()

   Busket = driver.find_element(By.PARTIAL_LINK_TEXT("busket"))
   time.sleep(2)
   oforml = driver.find_element(By.PARTIAL_LINK_TEXT("checkout"))
   time.sleep(2)

test_main()
driver.quit()

   


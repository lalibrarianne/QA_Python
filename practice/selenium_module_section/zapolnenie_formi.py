import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://erikdark.github.io/Qa_autotest_02/')
time.sleep(2)
input_one = driver.find_element(By.ID,'phone')
input_one.send_keys('89001233254')

input_two = driver.find_element(By.ID,'email')
input_two.send_keys('hokilo@mail.ru')

input_tri = driver.find_element(By.ID,'name')
input_tri.send_keys('Tomat')

input_four = driver.find_element(By.ID,'password')
input_four.send_keys('fkfirfh1553rdf')


btn = driver.find_element(By.ID,'submitBtn')

btn.click()
time.sleep(10)

driver.quit()



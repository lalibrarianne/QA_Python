import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get('https://erikdark.github.io/dovod_repo_QA_form/')
    data = ['admin123','password123','bd_dovod','localhost']
    inputs = driver.find_elements(By.TAG_NAME,'input')
    for i in range(len(inputs)):
        inputs[i].send_keys(data[i])
    btn = driver.find_element(By.TAG_NAME,'button')
    time.sleep(1)
    btn.click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    driver.find_element(By.CSS_SELECTOR, '#login').clear()
    driver.find_element(By.CSS_SELECTOR, '#password').clear()
    driver.find_element(By.CSS_SELECTOR, '#database').clear()
    driver.find_element(By.CSS_SELECTOR, '#host').clear()
    
    data = ['321nimda','321drowssap','dovod_db','tsohlacol']
    inputs = driver.find_elements(By.TAG_NAME,'input')
    for i in range(len(inputs)):
        inputs[i].send_keys(data[i])    

    btn = driver.find_element(By.TAG_NAME,'button')
    time.sleep(1)
    btn.click()
      
    time.sleep(3)
    driver.switch_to.alert.text('Вы прошли игру')
    

finally:
    driver.quit()



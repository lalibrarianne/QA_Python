import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/Qa_autotest_01/')
    time.sleep(2)
    input_one = driver.find_element(By.ID,'inputField')
    input_one.send_keys('Erik')


    buttons = driver.find_elements(By.CSS_SELECTOR, ".buttons .btn") 

    expected_button_count = 8 
      
    actual_button_count = len(buttons) 
     
    
    if actual_button_count == expected_button_count: 
        print(f"Количество кнопок совпадает: {actual_button_count}") 
    else: 
        print(f"Количество кнопок не совпадает: {actual_button_count} (ожидалось: {expected_button_count})") 
     
    
    if actual_button_count >= 3: 
        btn = buttons[2] 
        btn.click() 
        time.sleep(5) 
 
finally: 
    driver.quit() 



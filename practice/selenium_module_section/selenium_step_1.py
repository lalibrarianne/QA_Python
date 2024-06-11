import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
import re




#иницилизирую драйвер браузера
driver = webdriver.Chrome()




try:
    driver.get('https://erikdark.github.io/Qa_autotests_06/')
    time.sleep(2)
   
    nums = driver.find_element(By.CSS_SELECTOR,'#challenge')
    a = int(nums.get_attribute('data-a'))
    b = int(nums.get_attribute('data-b'))


    anser = a+b
   
    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(anser))


    driver.find_element(By.CSS_SELECTOR, '#notRobot').click()


    driver.find_element(By.CSS_SELECTOR, '#cool').click()


    driver.find_element(By.CSS_SELECTOR, '#submitBtn').click()




    text = driver.find_element(By.CSS_SELECTOR,'#message').text


    assert 'Поздравляю, Elon Musk!' == text


 


finally:
    time.sleep(5)
    driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


link = "https://erikdark.github.io/SHADOM-DOM-SELENIUM-QA/?name=df&email=EFE%40MAIL.RU"


class TestRegForm_negative(unittest.TestCase):
    def test_negative_1(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link)
            time.sleep(5)

            container = browser.find_element(By.ID, "shadow-host")
            container_shadow = container.shadow_root
            inputs = container_shadow.find_elements(By.CSS_SELECTOR, "input")

            # первое обязательное поле - имя:

            input_field = inputs[0]
            input_field.send_keys("Homa")
            time.sleep(3)
            input_field = inputs[1]
            input_field.send_keys("Homa@example.mail.ru")



            #browser.find_element(By.ID,'name').send_keys('Homa')
            #browser.find_element(By.ID,'email').send_keys('Homa@example.mail.ru')
            #time.sleep(3)
            browser.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
           
            # Очистка поля ввода
            browser.execute_script("arguments[0].value = 'Alisa'", input_field)


            # Для демонстрации
            time.sleep(2)
           
        finally:
            time.sleep(5)
            browser.quit()


if __name__ == "__main__":
    unittest.main()

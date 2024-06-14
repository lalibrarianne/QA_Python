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

            container = browser.find_element(By.CSS_SELECTOR, "#shadow-host")
            container_shadow = container.shadow_root
            container2 = container_shadow.find_element(By.CSS_SELECTOR,'div[id="shadow-host-two"]')
            container_shadow2 = container2.shadow_root
            inputs = container_shadow2.find_elements(By.CSS_SELECTOR, "input")

            input_field1 = inputs[0]
            input_field1.send_keys("Homa")
            
            input_field2 = inputs[1]
            input_field2.send_keys("Homa@example.mail.ru")
            time.sleep(3)
            
            browser.execute_script("arguments[0].value = 'Alisa'", input_field1)
            browser.execute_script("arguments[0].value = 'Alisa@no.com'", input_field2)

            time.sleep(2)
           
        finally:
            time.sleep(5)
            browser.quit()


if __name__ == "__main__":
    unittest.main()

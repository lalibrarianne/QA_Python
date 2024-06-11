import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

link = "https://erikdark.github.io/Qa_autotests_reg_form_pop_up/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():

    def login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#button").click()

    def autorisation(self, browser):
        browser.get(link)
        browser.find_element(By.ID, "openModalButton").click()
        input = browser.find_element(By.ID,'username')
        input.send_keys('testuser')
        input_pass = browser.find_element(By.ID,'password')
        input_pass.send_keys('password123')
        browser.find_element(By.CSS_SELECTOR, "#button").click()

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")

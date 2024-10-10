import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('chrome')
class TestsInputFields:
    TEXT: str = "--"
    EMAIL: str = "Faridun@gmail.ru"
    PASSWORD: str = "Its hard password with digital (132) and specific symbol (!)"

    def test_text_input(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Inputs").click()
        text_field = chrome.find_element(By.ID, "id_text_string")
        text_field.send_keys(self.TEXT)
        text_field.submit()
        result = chrome.find_element(By.ID, "result")

        assert self.TEXT in result.text, "String not found in result text"

    def test_email_field(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Inputs").click()
        chrome.find_element(By.LINK_TEXT, "Email field").click()
        email_field = chrome.find_element(By.ID, "id_email")
        email_field.send_keys(self.EMAIL)
        email_field.submit()
        result = chrome.find_element(By.ID, "result")

        assert self.EMAIL in result.text, "E-mail not found in result text"

    def test_password_field(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Inputs").click()
        chrome.find_element(By.LINK_TEXT, "Password field").click()
        email_field = chrome.find_element(By.ID, "id_password")
        email_field.send_keys(self.PASSWORD)
        email_field.submit()
        result = chrome.find_element(By.ID, "result")

        assert self.PASSWORD in result.text, "Password not found in result text"

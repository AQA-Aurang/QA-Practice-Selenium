import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('chrome')
class TestsButtons:
    SUBMITTED = "Submitted"
    ERROR_REASON = "Cannot find button or click on him"

    def test_simple_button(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Buttons").click()

        chrome.find_element(By.ID, "submit-id-submit").click()
        result = chrome.find_element(By.ID, "result")

        assert self.SUBMITTED in result.text, self.ERROR_REASON

    def test_looks_like_a_button(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Buttons").click()
        chrome.find_element(By.LINK_TEXT, "Looks like a button").click()

        chrome.find_element(By.LINK_TEXT, "Click").click()
        result = chrome.find_element(By.ID, "result")

        assert self.SUBMITTED in result.text, self.ERROR_REASON

    def test_disabled(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Buttons").click()
        chrome.find_element(By.LINK_TEXT, "Disabled").click()

        select_element = chrome.find_element(By.ID, "id_select_state")
        select = Select(select_element)
        select.select_by_value("enabled")

        chrome.find_element(By.ID, "submit-id-submit").click()
        result = chrome.find_element(By.ID, "result")

        assert self.SUBMITTED in result.text, self.ERROR_REASON

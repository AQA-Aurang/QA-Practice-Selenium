import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("chrome")
class TestsNewTabs:
    EXPECTED_RESULT = "I am a new page in a new tab"
    ERROR_REASON = "Cannot go to new page"

    def test_new_tab_link(self, chrome):
        chrome.find_element(By.LINK_TEXT, "New tab").click()
        chrome.find_element(By.ID, "new-page-link").click()
        tabs = chrome.window_handles
        current_tab = tabs[1]
        chrome.switch_to.window(current_tab)
        result = chrome.find_element(By.ID, "result")

        assert result.text in self.EXPECTED_RESULT, self.ERROR_REASON
        chrome.switch_to.window(tabs[0])

    def test_new_tab_button(self, chrome):
        chrome.find_element(By.LINK_TEXT, "New tab").click()
        chrome.find_element(By.LINK_TEXT, "New tab button").click()
        chrome.find_element(By.ID, "new-page-button").click()
        current_tab = chrome.window_handles[1]
        chrome.switch_to.window(current_tab)
        result = chrome.find_element(By.ID, "result")

        assert result.text in self.EXPECTED_RESULT, self.ERROR_REASON

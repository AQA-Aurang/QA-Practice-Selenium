import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("chrome")
class TestsAlerts:
    ERROR_REASON = "Cannot actions with alert"

    def test_alert_box(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Alerts").click()
        chrome.find_element(By.LINK_TEXT, "Click").click()
        confirm = chrome.switch_to.alert
        alert_text = confirm.text
        confirm.accept()

        assert "alert" in alert_text, self.ERROR_REASON

    @pytest.mark.parametrize("use_or_not", [True, False])
    def test_confirmation_box(self, chrome, use_or_not):
        chrome.find_element(By.LINK_TEXT, "Alerts").click()
        chrome.find_element(By.LINK_TEXT, "Confirmation box").click()
        chrome.find_element(By.LINK_TEXT, "Click").click()
        confirm = chrome.switch_to.alert

        if use_or_not:
            confirm.accept()
            choice = "Ok"
        else:
            confirm.dismiss()
            choice = "Cancel"

        result = chrome.find_element(By.ID, "result")

        assert choice in result.text, self.ERROR_REASON

    def test_prompt_box(self, chrome):
        text_for_alert = "Example text"
        chrome.find_element(By.LINK_TEXT, "Alerts").click()
        chrome.find_element(By.LINK_TEXT, "Prompt box").click()
        chrome.find_element(By.LINK_TEXT, "Click").click()
        confirm = chrome.switch_to.alert
        confirm.send_keys(text_for_alert)
        confirm.accept()

        result = chrome.find_element(By.ID, "result")

        assert text_for_alert in result.text, self.ERROR_REASON

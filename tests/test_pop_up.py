import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("chrome")
class TestsPopUpActions:
    ERROR_REASON_1ST_MODULE = "Cannot action with pop-up"
    ERROR_REASON_2ND_MODULE = "Cannot get text or get and put text in field"

    def test_modal_with_choice(self, chrome):
        element = chrome.find_element(By.LINK_TEXT, "Pop-Up")
        action_chains: ActionChains = ActionChains(chrome)
        action_chains.scroll_to_element(element).perform()
        element.click()

        chrome.find_element(By.XPATH, "(//button[@type='button'])[1]").click()
        chrome.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[2]").click()

        result = chrome.find_element(By.ID, "result")
        assert "None" in result.text, self.ERROR_REASON_1ST_MODULE

    def test_modal_without_choice(self, chrome):
        element = chrome.find_element(By.LINK_TEXT, "Pop-Up")
        action_chains: ActionChains = ActionChains(chrome)
        action_chains.scroll_to_element(element).perform()
        element.click()

        chrome.find_element(By.XPATH, "(//button[@type='button'])[1]").click()
        checkbox_and_title = chrome.find_element(By.XPATH, "(//div[@class='mb-3']//div)[2]")
        checkbox_and_title.find_element(By.ID, "id_checkbox_0").click()
        chrome.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[2]").click()

        result = chrome.find_element(By.ID, "result")
        assert "select me or not" in result.text, self.ERROR_REASON_1ST_MODULE

    def test_iframe_pop_up_with_copy(self, chrome):
        element = chrome.find_element(By.LINK_TEXT, "Pop-Up")
        action_chains: ActionChains = ActionChains(chrome)
        action_chains.scroll_to_element(element).perform()
        element.click()

        chrome.find_element(By.LINK_TEXT, "Iframe Pop-Up").click()
        chrome.find_element(By.XPATH, "(//button[@type='button'])[1]").click()

        iframe = chrome.find_element(By.CLASS_NAME, "embed-responsive-item")
        chrome.switch_to.frame(iframe)

        text_in_iframe = chrome.find_element(By.XPATH, "//div[@class='card card-body']")
        text: str = chrome.execute_script("return arguments[0].textContent;", text_in_iframe)
        text = text.strip()

        chrome.switch_to.default_content()

        chrome.find_element(By.XPATH, "//button[@form='empty-form']").click()
        some_text_field = chrome.find_element(By.ID, "id_text_from_iframe")
        some_text_field.send_keys(text)
        some_text_field.submit()

        result = chrome.find_element(By.ID, "check-result")
        assert "Correct" in result.text, self.ERROR_REASON_2ND_MODULE

    def test_iframe_pop_up_without_copy(self, chrome):
        element = chrome.find_element(By.LINK_TEXT, "Pop-Up")
        action_chains: ActionChains = ActionChains(chrome)
        action_chains.scroll_to_element(element).perform()
        element.click()

        chrome.find_element(By.LINK_TEXT, "Iframe Pop-Up").click()
        chrome.find_element(By.XPATH, "(//button[@type='button'])[1]").click()
        chrome.find_element(By.XPATH, "//button[@form='empty-form']").click()
        some_text_field = chrome.find_element(By.ID, "id_text_from_iframe")
        some_text_field.send_keys(" ")
        some_text_field.submit()

        result = chrome.find_element(By.ID, "check-result")
        assert "Nope" in result.text, self.ERROR_REASON_2ND_MODULE

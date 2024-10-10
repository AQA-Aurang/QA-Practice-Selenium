import pytest
from selenium.common import MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("chrome")
class TestsIframe:
    def test_iframe(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Iframes").click()

        iframe = chrome.find_element(By.CLASS_NAME, "embed-responsive-item")
        chrome.switch_to.frame(iframe)
        homepage = chrome.find_element(By.LINK_TEXT, "Visit the homepage")

        try:
            actions = ActionChains(chrome)
            actions.scroll_to_element(homepage).perform()
        except MoveTargetOutOfBoundsException as e:
            print("\n" + e.msg)

        homepage.click()
        h1 = chrome.find_element(By.TAG_NAME, "h1")

        assert "Hello" in h1.text, "Cannot get needed element in frame"
        chrome.switch_to.default_content()

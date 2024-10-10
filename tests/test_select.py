import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('chrome')
class TestsSelect:
    def test_single_select(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Select").click()

        select_element = chrome.find_element(By.ID, "id_choose_language")
        select = Select(select_element)
        select.select_by_visible_text("Python")

        chrome.find_element(By.ID, "submit-id-submit").click()
        result = chrome.find_element(By.ID, "result")

        assert "Python" in result.text, "Cannot select dropdown element"

    def test_multiple_select(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Select").click()
        chrome.find_element(By.LINK_TEXT, "Multiple selects").click()

        select_element = chrome.find_element(By.ID, "id_choose_the_place_you_want_to_go")
        select = Select(select_element)
        select.select_by_visible_text("Sea")

        select_element = chrome.find_element(By.ID, "id_choose_how_you_want_to_get_there")
        select = Select(select_element)
        select.select_by_visible_text("Air")

        select_element = chrome.find_element(By.ID, "id_choose_when_you_want_to_go")
        select = Select(select_element)
        select.select_by_visible_text("Today")

        submit_btn = chrome.find_element(By.ID, "submit-id-submit")
        action_chains: ActionChains = ActionChains(chrome)
        action_chains.scroll_to_element(submit_btn).perform()
        submit_btn.click()
        result = chrome.find_element(By.ID, "result")

        assert "sea" in result.text, "Cannot select 1st dropdown element"
        assert "air" in result.text, "Cannot select 2nd dropdown element"
        assert "today" in result.text, "Cannot select 3rd dropdown element"

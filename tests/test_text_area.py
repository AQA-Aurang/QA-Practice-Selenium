import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("chrome")
class TestsTextAreas:
    TEXT = "Some text in text area"
    TEXT_IN_1ST_CHAPTER = "Hey its text in the first chapter"

    def test_textarea(self, chrome):
        element = chrome.find_element(By.LINK_TEXT, "Text area")
        action_chains: ActionChains = ActionChains(chrome)
        action_chains.scroll_to_element(element).perform()
        element.click()

        textarea_element = chrome.find_element(By.ID, "id_text_area")
        textarea_element.send_keys(self.TEXT)
        textarea_element.submit()

        result = chrome.find_element(By.ID, "result")
        diff = len(result.text) - len(self.TEXT)
        new_result = result.text[diff:]

        assert new_result in self.TEXT, "Cannot get text in result"

    @pytest.mark.parametrize("chapters", [["second"], ["third"], ["second", "third"]])
    def test_multiple_textarea(self, chrome, chapters):
        element = chrome.find_element(By.LINK_TEXT, "Text area")
        action_chains: ActionChains = ActionChains(chrome)
        action_chains.scroll_to_element(element).perform()
        element.click()
        chrome.find_element(By.LINK_TEXT, "Multiple textareas").click()

        first_textarea = chrome.find_element(By.ID, "id_first_chapter")
        first_textarea.send_keys(self.TEXT_IN_1ST_CHAPTER)

        inputted_texts: list[str] = []
        for chapter in chapters:
            another_textarea = chrome.find_element(By.ID, f"id_{chapter}_chapter")
            text_in_another_chapter = f"Hey its text in the {chapter} chapter"
            inputted_texts.append(text_in_another_chapter)
            another_textarea.send_keys(text_in_another_chapter)

        first_textarea.submit()
        result = chrome.find_element(By.ID, "result")

        assert self.TEXT_IN_1ST_CHAPTER in result.text, "Cannot get text from 1st chapter"

        if len(inputted_texts) == 1:
            assert inputted_texts[0] in result.text, "Cannot get text from another chapter"
            return

        assert inputted_texts[0] in result.text, "Cannot get text from 2nd chapter"
        assert inputted_texts[1] in result.text, "Cannot get text from 3rd chapter"

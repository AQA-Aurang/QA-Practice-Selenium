import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('chrome')
class TestsCheckboxes:
    ERROR_REASON = "Cannot find or click on checkbox element"

    def test_single_checkbox(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Checkbox").click()

        checkbox_element = chrome.find_element(By.XPATH, "(//div[@class='mb-3']//div)[2]")
        checkbox_text = checkbox_element.text
        checkbox_element.find_element(By.ID, "id_checkbox_0").click()

        chrome.find_element(By.ID, "submit-id-submit").click()
        result = chrome.find_element(By.ID, "result")

        assert checkbox_text.lower() in result.text, self.ERROR_REASON

    @pytest.mark.parametrize("chkbx_id", [2, 3, 4])
    def test_checkboxes(self, chrome, chkbx_id):
        chrome.find_element(By.LINK_TEXT, "Checkbox").click()
        chrome.find_element(By.LINK_TEXT, "Checkboxes").click()

        checkbox_element = chrome.find_element(By.XPATH, f"(//div[@class='mb-3']//div)[{chkbx_id}]")
        checkbox_text = checkbox_element.text
        checkbox_element.find_element(By.ID, f"id_checkboxes_{chkbx_id-2}").click()

        chrome.find_element(By.ID, "submit-id-submit").click()
        result = chrome.find_element(By.ID, "result")

        assert checkbox_text.lower() in result.text, self.ERROR_REASON

    def test_all_checkboxes(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Checkbox").click()
        chrome.find_element(By.LINK_TEXT, "Checkboxes").click()
        list_of_title_selected_item = []

        for i in range(3):
            checkbox_element = chrome.find_element(By.XPATH, f"(//div[@class='mb-3']//div)[{i + 2}]")
            list_of_title_selected_item.append(checkbox_element.text)
            checkbox_element.find_element(By.ID, f"id_checkboxes_{i}").click()
        titles_in_str = ", ".join(list_of_title_selected_item)

        chrome.find_element(By.ID, "submit-id-submit").click()
        result = chrome.find_element(By.ID, "result")

        assert titles_in_str.lower() in result.text, self.ERROR_REASON

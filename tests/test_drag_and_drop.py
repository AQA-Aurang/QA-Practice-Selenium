from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("chrome")
class TestsDragAndDrops:
    EXPECTED_TEXT = "Dropped"
    ERROR_REASON = "Cannot drag and drop element"

    def test_boxes(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Drag and Drop").click()

        draggable_element = chrome.find_element(By.ID, "rect-draggable")
        droppable_element = chrome.find_element(By.ID, "rect-droppable")

        actions = ActionChains(chrome)
        actions.drag_and_drop(draggable_element, droppable_element).perform()

        dropped_element = chrome.find_element(By.ID, "rect-droppable")
        assert self.EXPECTED_TEXT in dropped_element.text, self.ERROR_REASON

    def test_images(self, chrome):
        chrome.find_element(By.LINK_TEXT, "Drag and Drop").click()
        chrome.find_element(By.LINK_TEXT, "Images").click()

        draggable_image = chrome.find_element(By.XPATH, "//div[@id='rect-droppable1']//img[1]")
        droppable_box = chrome.find_element(By.ID, "rect-droppable2")

        actions = ActionChains(chrome)
        actions.drag_and_drop(draggable_image, droppable_box).perform()

        dropped_element = chrome.find_element(By.ID, "rect-droppable2")
        assert self.EXPECTED_TEXT in dropped_element.text, self.ERROR_REASON

        sleep(3)

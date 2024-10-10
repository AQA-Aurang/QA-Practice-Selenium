import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

HOME_PAGE = "https://www.qa-practice.com/"


@pytest.fixture
def chrome_base():
    print("start browser for test")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get(HOME_PAGE)
    browser.find_element(By.XPATH, "//a[@href='javascript:;']").click()

    yield browser

    print("\nquit browser")
    browser.quit()


@pytest.fixture(scope="class")
def chrome(request):
    print("start browser for test")

    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get(HOME_PAGE)
    browser.find_element(By.XPATH, "//a[@href='javascript:;']").click()
    request.cls.driver = browser

    yield browser

    print("\nquit browser")
    browser.quit()

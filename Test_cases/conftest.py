import pytest
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

from Test_data import credentials
from Test_locators.test_locators import LoginPage_Locators, AdminPage_Locators

@pytest.fixture
def setup_browser():
    # This function sets up the browser before the test and yields it to the test function
    driver = webdriver.Chrome()
    driver.get(credentials.url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver  # This is the value that will be returned to the test function
    driver.quit()  # This will be executed after the test has finished

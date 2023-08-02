import logging
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
from selenium.webdriver.common.by import By
from Test_data import credentials
from Test_locators.test_locators import LoginPage_Locators

class LoginPage_Actions:

    def __init__(self, driver):   # Accept the WebDriver instance as an argument
        self.login_loc_obj = LoginPage_Locators()   # created an object for locator class
        self.driver = driver   # Use the WebDriver instance passed from the fixture


    def enter_username(self):
        """
        find the webelement for username ,clear the text field and set the username passed
        :return:
        """
        username_webelement = self.driver.find_element(By.NAME, self.login_loc_obj.username_loc_name)
        username_webelement.clear()
        username_webelement.send_keys(credentials.username)
        logging.info("Username entered")

    def enter_password(self):
        """
        find the webelement for password ,clear the text field and set the username passed
        :return:
        """
        password_webelement = self.driver.find_element(By.NAME, self.login_loc_obj.password_loc_name)
        password_webelement.clear()
        password_webelement.send_keys(credentials.password)
        logging.info("password entered")

    def click_login(self):
        login_button_webelement = self.driver.find_element(By.XPATH, self.login_loc_obj.login_loc_btn_xpath)
        login_button_webelement.click()
        logging.info("Login button clicked")

    def title_of_page(self):
        title_name = self.driver.title
        logging.info("Returning title of webpage", title_name)
        return self.driver.title

    # def capture_screenshot(driver, file_name):
    #     try:
    #         driver.save_screenshot(file_name)
    #         logging.info(f'Screenshot saved as {file_name}')
    #     except Exception as e:
    #         logging.error(f'Failed to capture screenshot: {str(e)}')

    def login_to_orangehrm(self):
        self.enter_username()
        self.enter_password()
        self.click_login()
        self.driver.implicitly_wait(20)


# if __name__ == '__main__':
#     LoginPageActions().login_to_orangehrm()
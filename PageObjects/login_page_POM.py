# import logging
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
from selenium.webdriver.common.by import By
from Test_data import credentials
from Test_locators.test_locators import orangehrm_LoginPageLocators

class orangehrm_LoginPageActions:

    def __init__(self, driver):   # Accept the WebDriver instance as an argument
        self.orange_loginlocators_obj = orangehrm_LoginPageLocators()   # created an object for locator class
        self.driver = driver   # Use the WebDriver instance passed from the fixture

    def enter_username(self):
        """
        find the webelement for username ,clear the text field and set the username passed
        :return:
        """
        username_webelement = self.driver.find_element(By.NAME, self.orange_loginlocators_obj.username_locator_name_tag)
        username_webelement.clear()
        username_webelement.send_keys(credentials.username)
        print("Username entered")

    def enter_password(self):
        """
        find the webelement for password ,clear the text field and set the username passed
        :return:
        """
        password_webelement = self.driver.find_element(By.NAME, self.orange_loginlocators_obj.password_locator_name_tag)
        password_webelement.clear()
        password_webelement.send_keys(credentials.password)
        print("password entered")

    def click_login(self):
        login_button_webelement = self.driver.find_element(By.XPATH, self.orange_loginlocators_obj.login_button)
        login_button_webelement.click()
        print("Login button clicked")

    def title_of_page(self):
        title_name = self.driver.title
        print("Returning title of webpage", title_name)
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
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from Test_data import credentials
from Test_locators.test_locators import AdminPage_Locators

class AdminPage_Actions:

    def __init__(self, driver):
        self.admin_loc_obj = AdminPage_Locators()  # created an object for locator class
        self.driver = driver

    def click_admin_menu(self, driver):
        """
        click on Admin menu item
        :return:
        """
        admin_we = self.driver.find_element(By.XPATH,self.admin_loc_obj.admin_locator_xpath)
        admin_we.click()




# import pytest
# import logging
from PageObjects.login_page_POM import LoginPage_Actions
from PageObjects.admin_page_POM import AdminPage_Actions
from Test_utilities.customLogger import logGen
class Test_AdminPage:

    def test_click_on_admin(self,setup_browser):
        """
        Clicking on Admin Menu Item
        :param setup_browser:
        :return:
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        LoginPage_Actions_obj = LoginPage_Actions(driver=setup_browser)  # Create an instance of orangehrm_LoginPageActions class
        AdminPage_Actions_obj = AdminPage_Actions(driver=setup_browser)

        LoginPage_Actions_obj.login_to_orangehrm()

        logs_obj.info("Clicking on Admin Menu Item")
        AdminPage_Actions_obj.click_admin_menu(driver=setup_browser)
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

        logs_obj.info("Entering username")
        AdminPage_Actions_obj.enter_username_admin()

        logs_obj.info("Selecting from userrole")
        AdminPage_Actions_obj.enter_userrole_dropdown_1()

        logs_obj.info("Entering EmployeeName")
        AdminPage_Actions_obj.enter_employeename()

        logs_obj.info("Selecting from Status")
        AdminPage_Actions_obj.status_dropdown()

        logs_obj.info("Click on ADD Button")
        AdminPage_Actions_obj.click_add_button()





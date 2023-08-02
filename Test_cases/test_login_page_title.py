# import logging
# import pytest
from PageObjects.login_page_POM import LoginPage_Actions
from Test_utilities.customLogger import logGen


class TestLoginTitle:
    def test_login_page_title(self, setup_browser):  # Pass the 'setup_browser' fixture as an argument
        """
        Testcase to test the title of our webpage
        :return:
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        LoginPage_Actions_obj = LoginPage_Actions(driver=setup_browser)  # Create an instance of orangehrm_LoginPageActions class

        # current_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # expected_url = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"
        logs_obj.info("Starting the Test")

        expected_title = 'orangehrm'
        LoginPage_Actions_obj.login_to_orangehrm()  # Call the method on the instance

        # Check the title of the page
        # assert orangehrm_LoginPageActions_obj.title_of_page() == expected_url

        current_page_title = LoginPage_Actions_obj.title_of_page()
        # # If the assertion fails, capture a screenshot
        # if orangehrm_LoginPageActions_obj.title_of_page() != expected_title:
        #     file_name = "screenshot_failed_assertion.png"
        #     orangehrm_LoginPageActions_obj.capture_screenshot(setup_browser, file_name)
        #     logGen.logger().info(f'Assertion failed. Captured screenshot: {file_name}')
        #
        if current_page_title == expected_title:
            logs_obj.info("*** Login Test Passed ***")
            logs_obj.info("Test Completed")
            self.driver.close()
            # assert True
        else:
            logs_obj.info("*** Login Test Failed ***")
            self.driver.save_screenshot("../Screenshots/Login_Failed.png")
            self.driver.close()
            # assert False
            logs_obj.info("Test Completed")

# TestLoginTitle().test_login_page_title()

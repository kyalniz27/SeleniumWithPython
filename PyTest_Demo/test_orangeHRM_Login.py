import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM",self.driver.title,"Title not matched")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.CSS_SELECTOR,"#txtUsername").send_keys("Admin")
        self.driver.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys("admin123")
        self.driver.find_element(By.CSS_SELECTOR,"#btnLogin").click()
        self.assertEqual("OrangeHRM", self.driver.title, "Title not matched")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        print("Test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..//Reports'))






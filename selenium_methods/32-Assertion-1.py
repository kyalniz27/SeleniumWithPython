import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testname1(self):
        self.driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
        self.driver.get("https://www.amazon.com")
        pageTitle = self.driver.title

        #assertEqual
        self.assertEqual("Amazon.com. Spend less. Smile more.",pageTitle,"Titles are not the same")
        self.driver.close()

    def testname2(self):
        self.driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
        self.driver.get("https://www.amazon.com")
        pageTitle = self.driver.title

        # assertNotEqual
        self.assertEqual("Amazon.com. Spend less. Smile more.", pageTitle, "Titles are the same")
        self.driver.close()


if __name__ == '__main__':
    unittest.main()        

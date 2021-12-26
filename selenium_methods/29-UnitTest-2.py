import unittest
from selenium import webdriver

class searchEngineTest(unittest.TestCase):
    def testAmazon(self):
        self.driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
        self.driver.get("https://www.amazon.com")
        print("Title of the page: " ,self.driver.title)
        self.driver.close()


    def test_google(self):
        self.driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
        self.driver.get("https://www.google.com")
        print("Title of the page: " , self.driver.title)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()




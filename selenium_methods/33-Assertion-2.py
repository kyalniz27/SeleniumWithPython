import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test1(self):
        self.driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
        self.driver.get("https://www.google.com")
        page_title = self.driver.title

        self.assertTrue(page_title == 'Google')
        self.driver.close()

    def test2(self):
        self.driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
        self.driver.get("https://www.google.com")
        page_title = self.driver.title

        self.assertFalse(page_title == 'Google')
        self.driver.close()

if __name__ == '__main__':
    unittest.main()




import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test1(self):
        driver = webdriver.Firefox(executable_path="C://Users//seker//Documents//driver//geckodriver.exe")
        #driver = None
        #self.assertIsNone(driver)
        self.assertIsNotNone(driver)

if __name__ == '__main__':
    unittest.main()




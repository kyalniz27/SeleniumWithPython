import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def test1(self):
        list = {'python', 'selenium', 'java'}
        self.assertIn('python',list)

    def test2(self):
        list = {'python', 'selenium', 'java'}
        self.assertNotIn('ruby',list)



if __name__ == '__main__':
    unittest.main()
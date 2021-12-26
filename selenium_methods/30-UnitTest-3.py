import unittest

def setUpModule():
    print('setUpModule')

def tearDownModule():
    print('tearDownModule')

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is Login test")

    @classmethod
    def tearDown(self):
        print('This is logout test')

    @classmethod
    def setUpClass(cls) -> None:
        print('Opening the application')

    @classmethod
    def tearDownClass(cls) -> None:
        print('Closing the application')

    def test_search(self):
        print('This is search test')

    def test_advancedSearch(self):
        print('This is advanced search test')

    def test_prepaidRecharge(self):
        print('This is prepaid recharge test')

    def test_postpaidRecharge(self):
        print('This is postpaid Recharge search test')


if __name__ == '__main__':
    unittest.main()
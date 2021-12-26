import unittest

class AppTesting(unittest.TestCase):

    def test_search(self):
        print('This is search test')

    @unittest.skip('I do not want advanced search that is why I am skipping this test')
    def test_advancedSearch(self):
        print('This is advanced search method')

    def test_prepaid(self):
        print('This is prepaid')

    def test_postpaid(self):
        print('This is post paid')

    @unittest.skipIf(1==1,'If 1 is equals 1 then skip it if not do not skip')
    def test_loginGmail(self):
        print('This login by gmail')

    @unittest.SkipTest
    def test_loginFacebook(self):
        print('This login by Facebook')


if __name__ == '__main__':
    unittest.main()    
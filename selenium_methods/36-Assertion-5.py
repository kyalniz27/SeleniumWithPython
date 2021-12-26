# Relational comparison
# assertGreater --> 1st value should be greater than the 2nd value in order to pass
# assertGreaterEqual --> 1st value should be greater or equal than the 2nd value in order to pass
# assertLess --> 1st value should be smaller than the 2nd value in order to pass
# assertLessEqual --> 1st value should be smaller or equal than the 2nd value in order to pass

import unittest

class Test(unittest.TestCase):
    def test1(self):
        #self.assertGreater(2,1)
        #self.assertGreaterEqual(10,10)
        self.assertLess(3,5)


if __name__ == '__main__':
    unittest.main()
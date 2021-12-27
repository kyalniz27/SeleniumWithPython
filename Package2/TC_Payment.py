import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentByCash(self):
        print("This is cash payment test")
        self.assertTrue(True)

    def test_paymentByCreditCard(self):
        print("This is credit card payment test")
        self.assertTrue(True)

    def test_paymentByDebitCard(self):
        print("This is debit card payment test")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()        
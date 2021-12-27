import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignUpTest import SignUpTest
from Package2.TC_Payment import PaymentTest
from Package2.TC_PaymentReturnTest import PaymentReturnTest

# Get all tests and initialize them
ts1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
ts2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
ts3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
ts4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

# Creating sanity and functional and master test suites and run them
sanityTestSuite = unittest.TestSuite([ts1,ts2])
functionalTestSuit = unittest.TestSuite([ts3,ts4])
masterTestSuite = unittest.TestSuite([ts1,ts2,ts3,ts4])

# Running test suites
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)







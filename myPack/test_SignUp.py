import pytest

@pytest.fixture()
def setUp():
    print("Opening URL to SignUp")
    yield
    print("Closing browser after SignUp")

def test_signUpByEmail(setUp):
    print("This is sign up by email test")

def test_signUpByFacebook(setUp):
        print("This is sign up by facebook test")
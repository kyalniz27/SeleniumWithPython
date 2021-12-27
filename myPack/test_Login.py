import pytest

@pytest.yield_fixture()
def setUp():
    print("Opening URL to Login")
    yield
    print("Closing browser after login")

def test_loginByEmail(setUp):
    print("This is login by email test")

def test_loginByFacebook(setUp):
        print("This is login by facebook test")

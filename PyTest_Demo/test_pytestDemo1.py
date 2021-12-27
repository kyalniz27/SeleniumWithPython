import pytest

@pytest.fixture()
def setUp():
    print("Once before every method")

def test_testDemo1(setUp):
    print('Test method 1')

def test_testDemo2(setUp):
    print('Test method 2')






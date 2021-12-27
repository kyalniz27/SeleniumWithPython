import pytest

@pytest.yield_fixture()
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")

def test_testDemo1(setUp):
    print('This is Test method 1')

def test_testDemo2(setUp):
    print('This is Test method 2')






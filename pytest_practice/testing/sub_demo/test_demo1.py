import pytest

@pytest.fixture()
def connectDB():
    print("test_demo1 connectDB")

def test_a(connectDB):
    print("sub_demo test_a")

def test_b(connectDB):
    print("sub_demo test_b")
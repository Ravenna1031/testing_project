# import pytest
#
#
# @pytest.fixture(scope='module')
# def connectDB():
#     print("连接数据库")
#     yield
#     print("断开数据库连接")


class TestDemo:

    def test_a(self, connectDB):
        print("测试用例a")

    def test_b(self, connectDB):
        print("测试用例b")

class TestDemo1:
    def test_c(self, connectDB):
        print("测试用例c")
"""
fixture定义
@pytest.fixture()
def fixture_method():
    print(setup操作)
    yield
    print(teardown操作)

调用方式
-测试用例中传入fixture方法名
-@pytest.mark.usefixtures("fixture方法名")
-自动调用 @pytest.fixture(autouse=True)

作用域
-控制方法 @pytest.fixture(scope="")
-scope取值
--function 默认值
--class
--module
--session

fixture方法返回值获取
-把返回值写到fixture方法的yield后面
-在测试用例中使用fixture方法名获取返回值
"""

import pytest

# 创建了登录的fixture方法
@pytest.fixture(autouse=True)
def login():
    print("登录操作")
    username = "eva"
    password = "123"
    token = "token123"
    yield [username, password, token]
    print("登出操作")


# 测试用例1：需要提前登录
def test_case1(connectDB):
    print(f"login info:{login}")
    print("测试用例1")


def test_case2():
    pass
"""
fixture的作用
定义传入测试中的数据集
配置测试前系统的初始状态
为批量测试提供数据源等

fixture的用法
1. 类似setup, teardown功能，但比setup, teardown更灵活
2. 直接通过函数名字调用或使用装饰器@pytest.mark.usefixture('test1')
3. 允许使用多个fixture
4. 使用autouse自动应用，如果要返回值，需要传fixture函数名
5. 作用域(session > module > class > function)

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

# 场景一： 自动化中应用
# 测试用例执行时，有的用例需要登录才能执行，有些用例不需要登录
# setup和teardown无法满足

# 场景2：yield
# 你已经可以将测试方法前要执行的或依赖的解决了
# 测试方法后销毁清除数据的要如何进行呢？


# 创建了登录的fixture方法
@pytest.fixture(scope="class")
def login():
    print("登录操作")
    username = "eva"
    password = "123"
    token = "token123"
    yield [username, password, token]
    print("登出操作")


# 测试用例1：需要提前登录
def test_case1(login):
    #print(f"login info:{login}")
    print("测试用例1")


def test_case2():
    print("测试用例2")

# 测试用例2：需要提前登录
def test_case3(login):
    print("测试用例3")

# 测试用例4：需要提前登录
@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")
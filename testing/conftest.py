# coding: utf-8
from typing import List

import pytest
import yaml
import os
from python_code.calc import Calculator
"""
conftest.py 用法
-conftest.py 文件名是不能改变的
-conftest.py 和要运行的用例需要在同一个包下面
-conftest.py 生效遵循就近原则

"""

# 获取yaml文件所在的绝对路径
yaml_path = os.path.dirname(__file__) + "/datas/calc.yaml"

@pytest.fixture(scope='session')
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库连接")


@pytest.fixture(scope="class")
def get_calc():
    # 获取计算机实例
    calc = Calculator()
    return calc


# 读取calc.yaml文件中 数据
with open(yaml_path, encoding='utf-8') as f:
    yaml_load = yaml.safe_load(f)
    # 加法用例数据
    ADD = yaml_load['add']
    add_data = ADD['data']
    add_id = ADD['id']
    # 减法用例数据
    SUB = yaml_load['sub']
    sub_data = SUB['data']
    sub_id = SUB['id']
    # 乘法用例数据
    MUL = yaml_load['mul']
    mul_data = MUL['data']
    mul_id = MUL['id']
    # 除法用例数据
    DIV = yaml_load['div']
    div_data = DIV['data']
    div_id = DIV['id']


@pytest.fixture(params=add_data, ids=add_id)
def get_add_data(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")


@pytest.fixture(params=sub_data, ids=sub_id)
def get_sub_data(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")


@pytest.fixture(params=mul_data, ids=mul_id)
def get_mul_data(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")


@pytest.fixture(params=div_data, ids=div_id)
def get_div_data(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")


"""
pytest hook 函数
-hook函数定义在conftest.py中
"""

# def pytest_collection_modifyitems(
#     session: "Session", config: "Config", items: List["Item"]
# ) -> None:
#     """Called after collection has been performed. May filter or re-order
#     the items in-place.
#
#     :param pytest.Session session: The pytest session object.
#     :param _pytest.config.Config config: The pytest config object.
#     :param List[pytest.Item] items: List of item objects.
#     """
#     print("items")
#     print(items)
#     items.reverse()
#
#     # 修改测试用例参数编码格式
#     for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')
#
#         # 自动给测试用例增加标签
#         # item.nodeid 拿到的是测试用例的名称
#         if 'add' in item.nodeid:
#             item.add_marker(pytest.mark.add)
#         elif 'div' in item.nodeid:
#             item.add_marker(pytest.mark.add)
#         elif 'sub' in item.nodeid:
#             item.add_marker(pytest.mark.sub)

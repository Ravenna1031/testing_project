# coding: utf-8

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

with open(yaml_path, encoding='utf-8') as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    add_id = datas['myid']
    # print(add_datas)

@pytest.fixture(params=add_datas, ids=add_id)
def get_add_datas(request):
    print("开始计算")
    data = request.param
    print(f"测试数据{data}")
    yield data
    print("结束计算")
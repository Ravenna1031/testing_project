<<<<<<< HEAD
"""
Pytest
单元测试，代码测试
web,app,接口以pytest为基础
python界比较主流的单元测试框架，unittest，pytest,nose……
入门难度低，第三方库丰富，通用性，与allure生成的报告非常的美观
"""
import pytest
import yaml

"""
pytest规则
测试文件、测试函数、测试方法，名称需要以test_开头
（函数-类的外面，方法-类的里面）
测试类名称需要Test开头
测试类中不能包含__init__方法

三种运行方式：
1. Pycharm界面运行

2. 右键文件/目录运行
2.1 运行整个测试文件：在文件上点击鼠标右键，选择run
2.2 点击绿色三角，运行对应的测试类或者测试方法

3. 使用命令行方式运行
3.1 运行当前目录下所有测试文件：‘pytest’
3.2 运行指定的测试文件：'pytest 文件名'
3.3 运行指定文件中的指定的类或者方法：'pytest 文件名::测试类名::测试方法'
3.4 查看执行过程中的详细信息和打印信息：'pytest -vs'
3.5 只收集测试用例不运行：‘pytest --collect-only’
3.6 生成执行结果文件：pytest --junitxml=./result.xml 
"""

"""
终端执行
pytest
pytest -v (最高级别信息 --verbose) 打印详细运行日志信息
pytest -v -s 文件名.py (s是带控制台输出结果，也是输出详细)
pytest 文件名.py 执行单独一个pytest模块
pytest 文件名.py::类名 运行某个模块里某个类
pytest 文件名.py::类名::方法名 运行某个模块里面某个类里面的方法

pytest -x 文件名 一旦运行到报错，就停止运行
pytest --maxfail=[num] 当运行错误达到num的时候就停止运行
pytest -k ”类名 and not 方法名“ 执行某个关键字的用例
pytest -m [标记名] @pytest.mark.[标记名]将运行有这个标记的测试用例

pytest --collect-only 只收集用例
pytest --junitxml=./result.xml 生成执行结果文件
pytest --setup-show 回溯fixture的执行国产
"""

"""
pytest框架结构
-模块级(setup_module/teardown_module)模块始末，全局的（优先最高）
-函数级(setup_function/teardown_function)只对函数用例生成（不在类中）
-类级(setup_class/teardown_class)只在类中前后运行一次（在类中）
-方法级(setup_method/teardown_method)开始于方法始末（在类中）
-类里面的（setup/teardown）运行在调用方法的前后
"""

"""
参数化与数据驱动
参数化：
待测试的输入和输出是一组输出，可以把测试数据组织起来，
用不同的测试数据调用相同的测试方法。
数据驱动：
数据驱动就是数据的改变从而驱动自动化测试的执行，最终引起测试结果的改变。

pytest参数化
参数化装饰函数
ids参数

参数化
-单个参数化：参数名称写在字符串中，参数值用列表传递
-多个参数：参数名称写在字符串中，参数值用列表套列表或者元组的方式传递
-测试用例起别名：ids=
-笛卡尔积：用两个装饰器分别传入参数
-从yaml中读取参数：数据读取成为参数化中需要的参数格式
"""



=======
# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_calc.py
import pytest
import yaml

>>>>>>> 08de4ac1693eec1200bebea48ddfc8ae2c855827
from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
<<<<<<< HEAD
    add_id = datas['myid']
=======
    print(add_datas)
    myid = datas['myid']
    print(myid)


def test_a():
    print("测试用例a")

>>>>>>> 08de4ac1693eec1200bebea48ddfc8ae2c855827

class TestCalc:

    def setup_class(self):
        print("开始计算")
        # 实例化计算器类
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a, b, expect",
<<<<<<< HEAD
        add_datas, ids=add_id
    )
    def test_add(self, a, b, expect):
        # # 实例化计算器类
        # calc = Calculator()
        # 调用add方法
        result = self.calc.add(a, b)
        # 判断result是浮点数，作出保留2位小数的处理
=======
        add_datas, ids=myid
    )
    def test_add(self, a, b, expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用 add 方法
        result = self.calc.add(a, b)
        # 判断 result 是浮点数，作出保留2为小数的处理
>>>>>>> 08de4ac1693eec1200bebea48ddfc8ae2c855827
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == expect

<<<<<<< HEAD
    # def test_add1(self):
    #     # # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用add方法
=======
    def test_add2(self):
        result = self.calc.add(0.1, 0.2)
        assert round(result, 2) == 0.3

    # def test_add1(self):
    #     # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用 add 方法
>>>>>>> 08de4ac1693eec1200bebea48ddfc8ae2c855827
    #     result = self.calc.add(0.1, 0.1)
    #     # 得到结果之后，需要写断言
    #     assert result == 0.2
    #
    # def test_add2(self):
<<<<<<< HEAD
    #     # # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用add方法
=======
    #     # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用 add 方法
>>>>>>> 08de4ac1693eec1200bebea48ddfc8ae2c855827
    #     result = self.calc.add(-1, -1)
    #     # 得到结果之后，需要写断言
    #     assert result == -2
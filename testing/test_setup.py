<<<<<<< HEAD
def setup_module():
    print("模块级别的setup")

def setup_module():
    print("模块级别的setup")

def teardown_module():
    print("模块级别的teardown")

def setup_function():
    print("函数级别的setup")

def teardown_function():
    print("函数级别的teardown")
=======
# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_setup.py

def setup_module():
    print("模块级别的 setup")


def teardown_module():
    print("模块级别的 teardown")


def setup_function():
    print("函数级别的 setup")


def teardown_function():
    print("函数级别的 teardown")

>>>>>>> 08de4ac1693eec1200bebea48ddfc8ae2c855827

def test_func1():
    print("测试函数1")


class TestDemo:

    def setup_class(self):
<<<<<<< HEAD
        print("类级别的setup")

    def teardown_class(self):
        print("类级别的teardown")

    def setup(self):
        print("方法级别的setup")

    def teardown(self):
        print("方法级别的teardown")

    def test_demo(self):
=======
        print("类级别的 setup")

    def teardown_class(self):
        print("类级别的 teardown")

    def setup(self):
        print("方法级别的 setup")

    def teardown(self):
        print("方法级别的 teardown")

    def test_demo1(self):
>>>>>>> 08de4ac1693eec1200bebea48ddfc8ae2c855827
        print("test_demo1")

    def test_demo2(self):
        print("test_demo2")

<<<<<<< HEAD
class TestDemo2:

    def setup_class(self):
        print("类级别的setup")

    def teardown_class(self):
        print("类级别的teardown")

    def setup(self):
        print("方法级别的setup")

    def teardown(self):
        print("方法级别的teardown")

    def test_demo(self):
        print("test_demo1")

    def test_demo2(self):
        print("test_demo2")
=======

class TestDemo2:

    def setup_class(self):
        print("类级别的 setup")

    def teardown_class(self):
        print("类级别的 teardown")

    def setup(self):
        print("方法级别的 setup")

    def teardown(self):
        print("方法级别的 teardown")

    def test_demo1(self):
        print("test_demo1")

    def test_demo2(self):
        print("test_demo2")
>>>>>>> 08de4ac1693eec1200bebea48ddfc8ae2c855827

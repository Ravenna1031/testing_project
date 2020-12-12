# -*- coding: utf-8 -*-


import pytest
from time import sleep
"""
分布式执行测试用例原理
-用例之间是独立的，用例之间没有依赖关系，用例可以完全独立运行
-用例执行没有顺序
-
"""
@pytest.mark.last
def test_foo():
    sleep(1)
    assert True

@pytest.mark.fourth
def test_bar():
    sleep(1)
    assert True

@pytest.mark.third
def test_ar():
    sleep(1)
    assert True



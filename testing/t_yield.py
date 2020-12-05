# coding: utf-8
import pytest


# yield生成器
def provider():
    # 循环读取数据列表
    for i in range(10):
        print("start")
        # 相当于return i，记录上一次执行的位置
        yield i
        print("end\n")


p = provider()
# 打印出来的对象类型就是生成器
# print(p)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
for i in p:
    print(i)
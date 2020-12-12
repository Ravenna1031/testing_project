# -*- coding: utf-8 -*-
from python_practice.send_gifts.send import send
from python_practice.send_gifts.show import show

"""
from … import 与 import 区别
1、 from…import 是复制了一份到本地
2、import … 是引用了变量的地址
"""
if __name__ == '__main__':
    send()
    show()

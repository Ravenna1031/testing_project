# -*- coding: utf-8 -*-
"""
发礼物
1. 拥有礼物的标识
2。定义一个发礼物的方法
3. 定义一个展示礼物的方法
4. 启动方法
"""

# 拥有礼物的标识
have_gift = False

# 发礼物方法
def send():
    print("发礼物")
    global have_gift
    have_gift = True

# 展示礼物
def show():
    if have_gift == True:
        print("收到礼物")
    else:
        print("没有礼物")

send()
show()
print(__name__)
if __name__ == '__main__':
    send()
    show()
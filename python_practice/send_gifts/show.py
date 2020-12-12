# -*- coding: utf-8 -*-
# from python_practice.send_gifts.gift import have_gift
import python_practice.send_gifts.gift as gitf

# 展示礼物
def show():
    if gitf.have_gift == True:
        print("收到礼物")
    else:
        print("没有礼物")
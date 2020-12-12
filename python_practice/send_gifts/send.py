# -*- coding: utf-8 -*-

from python_practice.send_gifts.gift import have_gift
import python_practice.send_gifts.gift as gift

# 发礼物方法
def send():
    print("发礼物")
    global have_gift
    gift.have_gift = True
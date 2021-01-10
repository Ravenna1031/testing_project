# -*- coding: utf-8 -*-
import pytest
from appium import webdriver
from hamcrest import *


class TestParm:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
        pass
    @pytest.mark.parametrize('search_key, code, price', [
        ('alibaba', 'BABA', 210),
        ('xiaomi', '01810', 30)
    ])
    def test_search(self, search_key, code, price):
        """
        1. 打开雪球应用
        2. 点击搜索框
        3. 输入搜索词
        4. 点击第一个搜索结果
        5. 判断股票价格
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(search_key)
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()
        current_price = self.driver.find_element_by_xpath(
            f"//*[@text='{code}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        expect_price = price
        current_price = float(current_price.text)
        print(current_price)
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))


# -*- coding: utf-8 -*-
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *


class TestLoc:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print("测试搜索用例")
        """
        1. 打开雪球app
        2. 点击搜索输入框
        3. 向输入框里输入“阿里巴巴”
        4. 再搜索结果里选择“阿里巴巴”，点击
        5. 获取阿里巴巴股价，判断股价价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']").click()
        price = float(self.driver.find_element_by_id("com.xueqiu.android:id/stock_current_price").text)
        # print(price)
        assert price > 200

    def test_attribute(self):
        """
        1. 打开雪球app
        2. 定位首页的搜索框
        3. 判断搜索框是否可用，查看搜索框name属性值
        4. 打印搜索框这个元素的左上角坐标和它的宽高
        5. 向搜索框输入：alibaba
        6. 判断阿里巴巴是否可见
        7. 如果可见，打印搜索成功，如何不可见，打印搜索失败
        """
        search = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search.text)
        print(search.location)
        print(search.size)
        if search.is_enabled():
            search.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touch(self):
        action = TouchAction(self.driver)
        width = self.driver.get_window_rect()['width']
        height = self.driver.get_window_rect()['height']
        action.press(x=width / 2, y=height * 0.8).wait(200).move_to(x=width / 2, y=height * 0.2).release().perform()

    def test_price(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        locator = (MobileBy.XPATH, "//*[@text=09988]/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        current_price = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        # current_price = self.driver.find_element_by_xpath(
        #     ).text
        # current_price = self.driver.find_element(*locator)
        print(current_price.text)
        expect_price = 210
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))
        # assert float(current_price) > 200
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("综合").fromParent(text("股票"))').click()

    def test_info(self):
        """
        1. 点击我的，进入到个人信息页面
        2。 点击登录，进入到登录页面
        3。 输入用户名，输入密码
        4. 点击登录
        """
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的").className("android.widget.TextView")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    def test_scroll_find(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("流水白菜").instance(0))').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("流水白菜")').click()

    def test_attribute(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("resource-id"))

    def test_hamcrest(self):
        # assert_that(10, equal_to(9), '提示')
        assert_that("contains string", contains_string("string"))


if __name__ == '__main__':
    pytest.main()

# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver

# 设备交互API
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestHCI:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        # desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # desired_caps['chromedriverExecutable'] = r'D:\Work\chromedriver_78.0.exe'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        # self.driver.make_gsm_call('13112341231', GsmCallActions.CALL)
        # self.driver.send_sms('13112341231', 'hello api')
        self.driver.set_network_connection(1)
        sleep(3)
        self.driver.set_network_connection(4)
        sleep(3)
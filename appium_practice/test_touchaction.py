# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestAction:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_unlock(self):
        action = TouchAction(self.driver)
        action.press(x=150, y=210).wait(200).move_to(x=450, y=210).wait(200).move_to(x=750, y=210).wait(200).move_to(
            x=750, y=520).wait(200).move_to(x=750,
                                            y=820).release().perform()

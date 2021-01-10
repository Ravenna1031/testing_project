# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHybird:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '11.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # desired_caps['noReset'] = 'true'
        # # desired_caps['dontStopAppOnReset'] = 'true'
        # desired_caps['skipDeviceInitialization'] = 'true'
        # desired_caps['unicodeKeyBoard'] = 'true'
        # desired_caps['resetKeyBoard'] = 'true'
        # desired_caps['chromedriverExecutable'] = r'D:\Work\chromedriver.exe'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_hybird(self):
        self.driver.find_element_by_xpath('//*[@text="交易"]').click()
        A_locator = (MobileBy.XPATH, '//*[@id="app"]/div/div/div/ul/li[1]/div[2]/h1')
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        print(self.driver.window_handles)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(A_locator))
        self.driver.find_element(*A_locator).click()

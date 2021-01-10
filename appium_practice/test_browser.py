# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            # 'browserName': 'Browser',
            'appPackage': 'io.appium.android.apis',
            'appActivity': 'io.appium.android.apis.ApiDemos',
            'noReset': True,
            'deviceName': '127.0.0.1:7555',
            'chromedriverExecutable': r'D:\Work\chromedriver.exe'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
        # pass

    def test_browser(self):
        self.driver.get('http://m.baidu.com/')
        self.driver.find_element_by_id('index-kw').click()
        self.driver.find_element_by_id('index-kw').send_keys('appium')
        search_btn = (By.ID, 'index-bn')
        search = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(search_btn))
        search.click()

    def test_webview(self):
        self.driver.find_element_by_accessibility_id('Views').click()
        webview = 'WebView'
        print(self.driver.contexts)
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{webview}").instance(0))').click()
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'i has no focus').send_keys("test string")
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'i am a link').click()
        sleep(1)
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID, 'i_am_a_textbox').send_keys('test string')
        self.driver.find_element(MobileBy.ID, 'i am a link').click()
        print(self.driver.page_source)
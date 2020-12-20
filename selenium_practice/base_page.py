# -*- coding: utf-8 -*-
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, base_url: WebDriver = None):
        # 避免driver重复初始化
        if base_url is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        else:
            self.driver = base_url

    def find_ele(self, by: WebDriver, locator: str):
        return self.driver.find_element(by, locator)

    def find_eles(self, by: WebDriver, locator: str):
        return self.driver.find_elements(by, locator)

    def wait_for_click(self, locator, timeout):
        element: WebDriver = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        return element

    def gender_click(self, gender):
        if gender == "male":
            return self.driver.find_element_by_name("gender")
        elif gender == "female":
            return self.driver.find_element_by_css_selector('.member_edit_sec:nth-child(1) .ww_label:nth-child(2) > .ww_radio')

    def element_exist(self, by: WebDriver, locator: str):
        ele = self.driver.find_elements(by, locator)
        if len(ele) == 0:
            return False
        elif len(ele) >= 1:
            return True


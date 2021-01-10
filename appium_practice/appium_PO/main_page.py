# -*- coding: utf-8 -*-
# 首页-点击通讯录
from appium_practice.appium_PO.addresslist_page import AddressListPage
from appium_practice.appium_PO.base_page import BasePage


class MainPage(BasePage):
    def click_addresslist(self):
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        return AddressListPage(self.driver)
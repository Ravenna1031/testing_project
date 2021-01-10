# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium_practice.appium_PO.base_page import BasePage
from appium_practice.appium_PO.member_inivte_page import MemberInivtePage


class AddressListPage(BasePage):
    def add_member(self):
        ele_add = self.driver.find_elements_by_xpath(
            '//*[contains(@text,"共")]')
        if len(ele_add) == 0:
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("共").instance(0));')
        self.driver.find_element_by_xpath(
            '//*[contains(@text,"共")]/../../android.widget.RelativeLayout[last()]').click()
        return MemberInivtePage(self.driver)

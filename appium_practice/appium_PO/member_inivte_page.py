# -*- coding: utf-8 -*-
# 点击手动输入添加
from appium_practice.appium_PO.base_page import BasePage
from appium_practice.appium_PO.contact_edit_page import ContactEditPage


class MemberInivtePage(BasePage):
    def add_manual(self):
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        return ContactEditPage(self.driver)

    def get_toast(self):
        toast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']")
        return toast.text

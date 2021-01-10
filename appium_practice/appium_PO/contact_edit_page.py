# -*- coding: utf-8 -*-
# 添加成员信息（姓名、性别、邮箱）
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from appium_practice.appium_PO.base_page import BasePage


class ContactEditPage(BasePage):
    def edit_name(self, input_name):
        name = self.driver.find_element_by_xpath("//*[contains(@text, '姓名')]/../android.widget.EditText")
        name.send_keys(input_name)
        return self

    def edit_gender(self, input_gender):
        gender = self.driver.find_element_by_xpath("//*[contains(@text, '性别')]/../android.widget.RelativeLayout")
        gender.click()
        female_locator = (MobileBy.XPATH, '//*[@text="女"]')
        male_locator = (MobileBy.XPATH, '//*[@text="男"]')
        female = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*female_locator))
        male = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*male_locator))
        if input_gender == "男":
            male.click()
        elif input_gender == "女":
            female.click()
        return self

    def edit_email(self, input_email):
        mail = self.driver.find_element_by_xpath("//*[contains(@text, '邮箱')]/../android.widget.EditText")
        mail.send_keys(input_email)
        return self

    def click_save(self):
        from appium_practice.appium_PO.member_inivte_page import MemberInivtePage
        self.driver.find_element_by_xpath("//*[contains(@text, '保存')]").click()
        return MemberInivtePage(self.driver)

# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_practice.base_page import BasePage
from selenium_practice.contact_po import ContactOP


class AddPO(BasePage):
    _init_name = (By.ID, "username")
    _init_nickname = (By.ID, "memberAdd_english_name")
    _init_id = (By.ID, "memberAdd_acctid")
    _init_cellphone = (By.ID, "memberAdd_phone")
    _init_phone = (By.ID, "memberAdd_telephone")
    _init_mail = (By.ID, "memberAdd_mail")
    _init_address = (By.ID, "memberEdit_address")
    _init_duty = (By.ID, "memberAdd_title")
    _init_save_btn = (By.CSS_SELECTOR, ".js_btn_save")
    _existing = (By.XPATH, '//*[@id="js_contacts220"]/div/div[2]/div/div[4]/div/form/div[2]/div[1]/div[2]/div[2]/div')
    _back = (By.XPATH, '//*[@id="js_contacts432"]/div/div[2]/div/div[4]/div/form/div[3]/a[3]')

    def add_member(self, **kwargs):
        # 姓名
        if kwargs['name'] != None:
            self.find_ele(*self._init_name).send_keys(kwargs['name'])
        # 别名
        if kwargs['nickname'] != None:
            self.find_ele(*self._init_nickname).send_keys(kwargs['nickname'])
        # 账号
        if kwargs['id'] != None:
            self.find_ele(*self._init_id).send_keys(kwargs['id'])
        # 性别
        if kwargs['gender'] != None:
            self.gender_click(kwargs['gender']).click()
        # 手机
        if kwargs['cellphone'] != None:
            self.find_ele(*self._init_cellphone).send_keys(kwargs['cellphone'])
        # 座机
        if kwargs['phone'] != None:
            self.find_ele(*self._init_phone).send_keys(kwargs['phone'])
        # 邮箱
        if kwargs['email'] != None:
            self.find_ele(*self._init_mail).send_keys(kwargs['email'])
        # 地址
        if kwargs['address'] != None:
            self.find_ele(*self._init_address).send_keys(kwargs['address'])
        # 职务
        if kwargs['duty'] != None:
            self.find_ele(*self._init_duty).send_keys(kwargs['duty'])
        # 保存
        self.find_ele(*self._init_save_btn).click()
        sleep(1)
        if self.element_exist(*self._existing):
            self.find_ele(*self._back).click()
            return ContactOP(self.driver)
        else:
            return ContactOP(self.driver)

    def add_member_fail(self):
        # 重复数据 优化
        return ContactOP(self.driver)

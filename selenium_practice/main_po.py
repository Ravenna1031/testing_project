# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_practice.base_page import BasePage
from selenium_practice.contact_po import ContactOP
from selenium_practice.add_po import AddPO


class MainPO(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def go_to_contact(self):
        # self.driver.find_element_by_id("menu_contacts").click()
        self.find_ele(By.ID, "menu_index").click()
        sleep(1)
        self.find_ele(By.ID, "menu_contacts").click()
        return ContactOP(self.driver)

    def go_to_contact_from_main(self):
        self.find_ele(By.ID, "menu_index").click()
        sleep(1)
        self.find_ele(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        return AddPO()

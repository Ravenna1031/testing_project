# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_practice.base_page import BasePage


class ContactOP(BasePage):
    def click_add_member(self):
        from selenium_practice.add_po import AddPO
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        self.wait_for_click(ele, 10)
        while True:
            # ele = driver.find_element_by_css_selector(".ww_operationBar .js_add_member")
            self.driver.find_element(*ele).click()
            # ele.click()
            element = self.find_eles(By.ID, "username")
            if len(element) > 0:
                break
        return AddPO(self.driver)

    def get_member(self):
        sleep(1)
        eles = self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for value in eles:
            print(value.get_attribute("title"))
            name_list.append(value.get_attribute("title"))
        # assert "uuu" in name_list
        return name_list

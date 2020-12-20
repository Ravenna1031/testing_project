# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        # 点击
        action.click(element_click)
        # 右键点击
        action.context_click(element_rightclick)
        # 双击
        action.double_click(element_doubleclick)
        # 执行
        sleep(3)
        action.perform()
        sleep(3)

    def test_move(self):
        self.driver.get("https://www.baidu.com/")
        # 有些可以点击的链接跳转上面的文字，就是link text
        ele = self.driver.find_element_by_link_text("登录")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    def test_drag(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele = self.driver.find_element_by_id("dragger")
        drop_ele = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_ele, drop_ele)
        # action.click_and_hold(drag_ele).release(drop_ele)
        action.click_and_hold(drag_ele).move_to_element(drop_ele).release()
        action.perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        input_ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        input_ele.click()
        action = ActionChains(self.driver)
        action.send_keys("user").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("name").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

    def test_touch_scroll(self):
        self.driver.get("https://www.baidu.com/")
        search = self.driver.find_element_by_id("kw")
        search.send_keys("selenium")
        action = TouchActions(self.driver)
        btn = self.driver.find_element_by_id("su")
        action.tap(btn)
        action.perform()
        action.scroll_from_element(btn, 0, 9999).perform()
        # sleep(3)

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("123")
        self.driver.find_element_by_id("user_password").send_keys("password")
        self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        sleep(3)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_action.py'])

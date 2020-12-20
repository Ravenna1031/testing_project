# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login():
    # 调用chromeoptions方法
    opt = webdriver.ChromeOptions()
    # 设置复用浏览器的地址
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    driver.find_element_by_id("menu_contacts").click()
    ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(ele))
    while True:
        # ele = driver.find_element_by_css_selector(".ww_operationBar .js_add_member")
        driver.find_element(*ele).click()
        # ele.click()
        element = driver.find_elements_by_id("username")
        if len(element) > 0:
            break
    driver.find_element_by_id("username").send_keys("uuu")
    driver.find_element_by_id("memberAdd_acctid").send_keys("xxuuds")
    driver.find_element_by_id("memberAdd_mail").send_keys("123@qq.com")
    driver.find_element_by_css_selector(".js_btn_save").click()
    time.sleep(1)
    eles = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
    name_list = []
    for value in eles:
        print(value.get_attribute("title"))
        name_list.append(value.get_attribute("title"))
    # assert "uuu" in name_list
    return name_list

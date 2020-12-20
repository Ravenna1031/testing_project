# -*- coding: utf-8 -*-
from selenium import webdriver
import yaml
from time import sleep


# cmd
# chrome --remote-debugging-port=9222


# 获取cookie
def test_get_cookie():
    # 调用chromeoptions方法
    opt = webdriver.ChromeOptions()
    # 设置复用浏览器的地址
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    cookies = driver.get_cookies()
    # 覆盖写入
    with open("cookie.yaml", "w", encoding="utf-8") as f:
        # 快捷键import： alt + enter
        yaml.dump(cookies, f)


class TestDemo():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("cookie.yaml", encoding="utf-8") as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            # 把cookie传给driver
            self.driver.add_cookie(cookie)
        # 设置cookie后，再次访问企业微信
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 点击 通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        # 点击 添加成员
        sleep(1)
        self.driver.find_elements_by_xpath('//*[@class="ww_operationBar"]/a')[0].click()
        # 姓名 输入“测试姓名”
        self.driver.find_element_by_id("username").send_keys("测试姓名")
        # 账号 输入“test1”
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("test1")
        # 收集 输入“13110101010”
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13110101010")
        # 点击 保存
        sleep(1)
        self.driver.find_elements_by_xpath('//*[@class="member_colRight_operationBar ww_operationBar"]/a')[0].click()
        sleep(3)

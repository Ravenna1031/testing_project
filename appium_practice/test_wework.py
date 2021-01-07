# -*- coding: utf-8 -*-


# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver

# caps = {}
# caps["platformName"] = "Android"
# caps["deviceName"] = "127.0.0.1:7555"
# caps["appPackage"] = "com.tencent.wework"
# caps["appActivity"] = ".launch.LaunchSplashActivity"
# caps["ensureWebviewsHavePages"] = True
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#
# el1 = driver.find_element_by_id("com.tencent.wework:id/hz5")
# el1.click()
# el1.click()
# el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.TextView")
# el2.click()
# el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.TextView")
# el3.click()
# el3.click()
#
# driver.quit()
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class TestWework:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["ensureWebviewsHavePages"] = True
        caps["noReset"] = True
        caps['settings[waitForIdleTimeout]'] = 0

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element_by_xpath('//*[@text="工作台"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("打卡").instance(0));').click()

        self.driver.find_element_by_xpath('//*[@text="外出打卡"]').click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
        r = self.driver.find_element_by_id("com.tencent.wework:id/pt").text
        assert r == "外出打卡成功"

    def test_add_member(self):
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        ele_add = self.driver.find_elements_by_xpath(
            '//*[contains(@text,"共")]')
        if len(ele_add) == 0:
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("共").instance(0));')
        self.driver.find_element_by_xpath(
            '//*[contains(@text,"共")]/../../android.widget.RelativeLayout[last()]').click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        # 姓名
        name = self.driver.find_element_by_xpath("//*[contains(@text, '姓名')]/../android.widget.EditText")
        name.send_keys("Van")
        # 性别
        gender = self.driver.find_element_by_xpath("//*[contains(@text, '性别')]/../android.widget.RelativeLayout")
        gender.click()
        female_locator = (MobileBy.XPATH, '//*[@text="女"]')
        female = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*female_locator))
        female.click()
        # 手机
        phone_number = self.driver.find_element_by_xpath("//*[contains(@text, '手机号')]")
        phone_number.send_keys("13510191010")
        # 邮箱
        mail = self.driver.find_element_by_xpath("//*[contains(@text, '邮箱')]/../android.widget.EditText")
        mail.send_keys("abc456@qq.com")
        # 地址
        self.driver.find_element_by_xpath("//*[contains(@text, '地址')]/../android.widget.RelativeLayout").click()
        self.driver.find_element_by_xpath("//*[contains(@text, '请输入公司地址')]").send_keys("上海市精神卫生")
        address_locator = (MobileBy.XPATH, "//*[contains(@text, '宛平南路600号')]")
        address = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*address_locator))
        address.click()
        self.driver.find_element_by_xpath("//*[contains(@text, '确定')]").click()
        # 部门
        self.driver.find_element_by_xpath("//*[contains(@text, '设置部门')]").click()
        yes_locator = (MobileBy.XPATH, '//*[contains(@text, "确定")]')
        yes = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*yes_locator))
        yes.click()
        # 身份
        role = self.driver.find_element_by_xpath("//*[contains(@text, '身份')]/../android.widget.RelativeLayout")
        role.click()
        leader_locator = (MobileBy.XPATH, '//*[contains(@text, "上级")]')
        leader = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*leader_locator))
        leader.click()
        # 保存
        self.driver.find_element_by_xpath("//*[contains(@text, '保存')]").click()
        # Toast
        toast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']")
        assert toast.text == '添加成功'
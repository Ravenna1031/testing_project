# -*- coding: utf-8 -*-
# 启动app、关闭app、重启app、进入首页
from appium import webdriver

from appium_practice.appium_PO.base_page import BasePage
from appium_practice.appium_PO.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
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
        else:
            # 根据caps内设置的app信息启动app
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def enter_main(self) -> MainPage:
        return MainPage(self.driver)

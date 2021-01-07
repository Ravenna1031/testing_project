# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
desired_caps['noReset'] = 'true'
desired_caps['dontStopAppOnReset'] = 'true'
desired_caps['skipDeviceInitialization'] = 'true'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.back()
driver.back()
driver.quit()
# desire_cap = {
#     "platformName": "Android",
#     "deviceName": "127.0.0.1:7555",
#     "appPackage": "com.xueqiu.android",
#     "appActivity": ".view.WelcomeActivityAlias",
#     # 不要对应用进行reset
#     "noReset": True
# }
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
# driver.implicitly_wait(10)
# el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
# el1.click()
# el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
# el2.send_keys("alibaba")
# el3 = driver.find_element_by_xpath(
#     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
# el3.click()

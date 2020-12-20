# -*- coding: utf-8 -*-
from time import sleep

from selenium_practice.main_po import MainPO


class TestLogin:
    def setup(self):
        self.main = MainPO()

    def teardown(self):
        pass

    def test_login(self, get_user_data):
        # 链式调用
        # 不要在页面中断言，要在case中断言
        # name_list = self.main.go_to_contact().click_add_member().add_member(**get_user_data).get_member()
        name_list = self.main.go_to_contact().click_add_member().add_member(**get_user_data).get_member()
        print(name_list)
        # print(get_user_data['name'])
        assert get_user_data['name'] in name_list

    def test_add_from_main(self, get_user_data):
        name_list = self.main.go_to_contact_from_main().add_member(**get_user_data).get_member()
        print(name_list)
        # assert

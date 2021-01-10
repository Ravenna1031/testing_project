# -*- coding: utf-8 -*-
# 测试用例
import pytest
import yaml

from appium_practice.appium_PO.app import App

def get_data():
    with open('data.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        add_number = data['add']
        return add_number

class TestAddMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().enter_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize('name, gender, email', get_data())
    def test_add_contact(self, name, gender, email):
        toast = self.main.click_addresslist().add_member().add_manual().edit_name(name).edit_gender(gender).edit_email(email).click_save().get_toast()
        print(toast)
        assert toast == '添加成功'
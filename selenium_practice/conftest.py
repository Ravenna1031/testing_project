# -*- coding: utf-8 -*-
import pytest
import yaml

with open('login.yaml', encoding="GBK") as f:
    yaml_data = yaml.safe_load(f)
    user_info = yaml_data['user_data']
    id_info = yaml_data['ids']


@pytest.fixture(params=user_info, ids=id_info)
def get_user_data(request):
    print("用例执行开始")
    data = request.param
    yield data
    print("用例执行结束")

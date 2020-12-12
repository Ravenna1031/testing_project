import pytest

# 参数化
@pytest.fixture(params=[1, 2, 3])
def login1(request):
    data = request.param
    #print(request.param)
    print("获取测试数据")
    return data + 1


# 通过不同数据生成不同测试用例
def test_case1(login1):
    print(login1)
    print("测试用例1")

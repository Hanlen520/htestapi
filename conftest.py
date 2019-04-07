import pytest
import json
from common.commonData import CommonData
from util.httpUtil import HttpUtil
http =HttpUtil()
@pytest.fixture(scope='session',autouse=True)  #session全局初始化操作
def session_fixture():
    path="/sys/login"
    data={"userName":CommonData.mobile,"password": CommonData.password}
    resp_login=http.post(path,data)
    CommonData.token= resp_login['object']['token']  # 获取token
    print("登录成功")


    yield
    path="/sys/logout"
    resp_logout=http.post(path)
    assert resp_logout['code']==200
    print("退出登录")



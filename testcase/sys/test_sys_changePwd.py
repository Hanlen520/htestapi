from common.commonData import CommonData
from conftest import http
import pytest
import allure
@allure.feature('修改密码模块')
class Test_ChangePwd:
    @allure.story('修改密码成功')
    @pytest.mark.usefixtures("reset")
    def test_changepwd_success(self):
        data = {
            'token': CommonData.token,
            'userId':160,
            'userName': CommonData.mobile,
            'oldPwd': CommonData.password,
            'password':"456789"
        }
        resp =http.post("/sys/changePwd",data)
        assert resp['code']==200
        assert resp['msg'] == "操作成功"
@allure.story('重置密码成功')
@pytest.fixture()
def reset():
    yield
    data = {
        'token': CommonData.token,
        'userId':160,
        'userName': CommonData.mobile,
        'oldPwd': "456789",
        'password':CommonData.password
    }
    resp =http.post("/sys/changePwd",data)
    assert resp['code']==200
    assert resp['msg'] == "操作成功"

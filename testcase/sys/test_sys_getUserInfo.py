from common.commonData import CommonData
from conftest import http
import allure
@allure.feature('获取用户信息模块')
class Test_GetUserInfo:
    @allure.story('获取用户信息')
    def test_getUserInfo(self):
        path = "/sys/getUserInfo"
        data={'token':CommonData.token}
        resp =http.post(path,data)
        assert resp['code']==200
        assert resp['msg'] == "操作成功"
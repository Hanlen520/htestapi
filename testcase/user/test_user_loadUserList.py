from common.commonData import CommonData
from conftest import http
import allure
@allure.feature('加载用户列表模块')
class Test_LoadUserList:
    @allure.story('加载用户列表成功')
    def test_loaduserlist(self):
        path = "/user/loadUserList"
        data={
            "token":CommonData.token,
            "pageCurrent": 1,
            "pageSize": 10,
            "nickName": "",
            "userName": "",
            "regionId": 1
        }
        resp =http.post(path,data)
        assert resp['code']==200
        assert resp['msg'] == "操作成功"
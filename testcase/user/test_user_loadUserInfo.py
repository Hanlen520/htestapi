from common.commonData import CommonData
from conftest import http
import pytest
class Test_Login:
    @pytest.mark.debug
    def test_adduser(self):
        #注册
        add_data = {

            "nickName": CommonData.add_nickName,
            "userName": CommonData.add_user,
            "telNo": "",
            "email": "",
            "address": "",
            "roleIds": "1",
            "regionId": 1,
            "regionLevel": 1
        }
        resp_add =http.post("/user/saveOrUpdateUser",add_data)
        print(resp_add)
        # assert resp_add['code']==200
        # assert resp_add['msg']=="操作成功"
        #新账户登录
        data_login = {
            'userName': CommonData.add_user,
            'password': CommonData.password
        }
        resp_login = http.post("/sys/login", data_login)
        assert resp_login['code'] == 200
        assert resp_login['msg'] == "操作成功"
        adduser_id=resp_login['object']['userId']


        #查看用户列表
        data_check = {

            "pageCurrent": 1,
            "pageSize": 10,
            "nickName": "",
            "userName": "",
            "regionId": 1
        }
        resp_check= http.post("/user/loadUserList", data_check)
        assert resp_check['object']['list'][0]['id'] == adduser_id
        assert resp_check['object']['list'][0]['nickName'] == CommonData.add_nickName
        #查看用户详情
        data_userinfo = {
	        "id": adduser_id
        }
        resp_userinfo=http.post("/user/loadUserInfo", data_userinfo)
        assert resp_userinfo['code']==200
from common.commonData import CommonData
from conftest import http
import allure
@allure.feature('登录模块')
class Test_Login:
    @allure.story('登录成功')
    def test_login_success(self):
        data = {
            'userName': CommonData.mobile,
            'password': CommonData.password
        }
        resp =http.post("/sys/login",data)
        assert resp['code']==200
        assert resp['msg']=="操作成功"
        assert resp['object']['userId']==160

    @allure.story('密码错误')
    def test_login_Pfail(self): #密码错误
        data = {
            'userName': CommonData.mobile,
            'password': "1234567"
        }
        resp =http.post("/sys/login",data)
        assert resp['code']==410
        assert resp['msg']=="用户名或密码错误"

    @allure.story('用户名错误')
    def test_login_Ufail(self): #用户名错误
        data = {
            'userName': "15456542563",
            'password': CommonData.password
        }
        resp =http.post("/sys/login",data)
        assert resp['code']==301
        assert resp['msg']=="用户不存在"

    @allure.story('用户名为空')
    def test_login_username_none(self):  #用户名为空
        data={
            'userName': '',
            'password': CommonData.password
        }
        resp = http.post("/sys/login", data)
        assert resp['code'] == 301

    @allure.story('密码为空')
    def test_login_password_none(self):  #密码为空
        data={
            'userName': CommonData.mobile,
            'password': ''
        }
        resp = http.post("/sys/login", data)
        assert resp['code'] == 410
        assert resp['msg'] == "用户名或密码错误"

    @allure.story('用户名包含特殊字符')
    def test_login_username_special(self): #用户名包含特殊字符
        data = {
            'userName': '#$%#^',
            'password': CommonData.password
        }
        resp = http.post("/sys/login", data)
        assert resp['code'] == 301
        assert resp['msg'] == "用户不存在"

    @allure.story('用户名过长')
    def test_login_username_long(self): #用户名过长
        data = {
            'userName': '15644132154562123',
            'password': CommonData.password
        }
        resp = http.post("/sys/login", data)
        assert resp['code'] == 301
        assert resp['msg'] == "用户不存在"
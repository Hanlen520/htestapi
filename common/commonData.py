import random
class CommonData:
    mobile="15935117527"
    password="123456"
    host="http://192.168.1.203:8083"
    token=None
    proxies = {"http": "http://localhost:8888"}


    add_nickName=str(random.randint(10000000,100000000))
    add_user = "159" + add_nickName
import base64

import pytest
import allure

from common.send_request import SendRequest
from common.yaml_util import read_testcase_yaml, write_yaml, read_yaml
from redisopts.redis_conf import RedisConf
from Crypto.Cipher import AES


class TestLoginApi:
    # 类遍量，通过类名来访问

    # 获取鉴权码
    # @allure.feature("获取验证码图片")
    # @allure.story("story:正向测试用例")
    # @allure.severity("P1")
    # @allure.title("获取验证码图片接口")
    # @allure.description("用例描述：获取数字运算图片 01")
    def test_code(self):
        print("获取图片验证码")
        url = "http://wxhl.test.geointech.cn:10001/code"
        method = "get"
        res = SendRequest().all_send_request(
            method=method,
            url=url
        )
        result = res.json()

        # uuid写入到全局变量中
        write_yaml({"uuid": result["uuid"]})
        # print(read_yaml("uuid"))

    # 获取code值
    # @allure.feature("获取图片验证码内容")
    # @allure.story("story:正向测试用例")
    # @allure.severity("P1")
    # @allure.title("获取图片验证码内容")
    # @allure.description("用例描述：获取图片验证码内容")
    def test_getCode(self):
        print("获取code值")
        res = eval(RedisConf.getCode(read_yaml("uuid_pre") + read_yaml("uuid")))
        write_yaml({"code": res})
        print("\n")

    # 登录
    # @allure.feature("登录")
    # @allure.story("story:正向测试用例")
    # @allure.severity("blocker")
    # @allure.title("登录")
    # @allure.description("用例描述：登录成功")
    @pytest.mark.parametrize("login", read_testcase_yaml("./login.yaml"))
    def test_login(self, login):
        print(login["name"])
        url = login["request"]["url"]
        method = login["request"]["method"]
        headers = login["headers"]
        BLOCK_SIZE = 16
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                        chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
        secret = '[geoin-building]'
        iv = '[geoin-building]'
        password = login["params"]["password"]
        data = pad(password)
        aes = AES.new(secret.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))
        text = aes.encrypt(data.encode('utf-8'))
        encodestr = base64.b64encode(text)
        pwd = encodestr.decode('utf8')
        _data = {
            "username": login["params"]["username"],
            "password": pwd,
            "code": read_yaml("code"),
            "uuid": read_yaml("uuid")
        }
        # self.test_code()
        # self.test_getCode()
        res = SendRequest().all_send_request(
            method=method,
            url=url,
            json=_data,
            headers=headers
        )

        result = res.json()
        if result["code"] == login["result"]["code"]:
            if result["code"] == 200:
                datajson = result["data"]
                write_yaml({"access_token": datajson["access_token"]})
                print("登录成功" + "\n")
                print(result)
            else:
                print("接口正常" + "\n")
        else:
            print(result["msg"] + "\n")

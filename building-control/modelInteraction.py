import pytest

from common.send_request import SendRequest
from common.yaml_util import read_testcase_yaml, read_yaml


class TestControlApi:
    # 获取所选择设备的主要运行状态信息和参数
    @pytest.mark.parametrize("queryDeviceInfo", read_testcase_yaml("./queryDeviceInfo.yaml"))
    def test_queryDeviceInfo(self, queryDeviceInfo):
        print(queryDeviceInfo["name"])
        url = queryDeviceInfo["request"]["url"]
        method = queryDeviceInfo["request"]["method"]
        headers = {
            "Content-Type": queryDeviceInfo["headers"]["Content-Type"],
            "token": read_yaml("access_token")
        }
        res = SendRequest().all_send_request(
            method=method,
            url=url,
            json=queryDeviceInfo["params"]["modelId"],
            headers=headers
        )
        result = res.json()
        print(result)
        if result["code"] == 200:
            print("请求成功" + "\n")

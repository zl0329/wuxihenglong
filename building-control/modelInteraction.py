import pytest

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

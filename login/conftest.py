import pytest

from common.yaml_util import clear_yaml, write_yaml


@pytest.fixture(scope="session", autouse=True)
def exe_assert():
    clear_yaml()
    write_yaml({"username": "HLadmin123"})
    write_yaml({"uuid_pre": "captcha_codes:"})
    write_yaml({"password": "HLadmin123"})
    yield
    print("-" * 100)

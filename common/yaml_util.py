import os

import yaml


# 读取yaml文件
def read_yaml(key):
    with open(r"E:\PycharmProjects\wuxihenglong\extract.yaml", encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


# 写入yaml文件
def write_yaml(data):
    with open(r"E:\PycharmProjects\wuxihenglong\extract.yaml", encoding="utf-8", mode="a") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 清空yaml文件内容
def clear_yaml():
    with open(r"E:\PycharmProjects\wuxihenglong\extract.yaml", encoding="utf-8", mode="w") as f:
        f.truncate()


# 读取所有的yaml内容
def read_all_yaml():
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


# 读取所有yaml内容
def read_testcase_yaml(yaml_path):
    with open(os.getcwd() + yaml_path, encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value

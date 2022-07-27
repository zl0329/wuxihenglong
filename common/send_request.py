# 封装
import requests


class SendRequest:
    # 会话，会话对象会自动去管理Cookie关联，
    sess = requests.session()
    print(sess)

    def all_send_request(self, method, url, **kwargs):
        print("接口测试开始------------------------")
        print("请求方式：%s" % method)
        print("请求地址：%s" % url)
        res = SendRequest.sess.request(method, url, **kwargs)
        print("接口测试结束------------------------")
        print("\n")
        return res

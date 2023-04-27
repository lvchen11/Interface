import unittest

import requests
import json


class IntergrateRequest(unittest.TestCase):
    # 请求 request方法
    def get_req(self, url, data, headers):
        if headers is not None:
            res = requests.get(url, headers=headers, data=data).json()
        else:
            res = requests.get(url, data).json()
        return res

    # post 请求方式
    def post_req(self, url, data, headers):
        if headers is not None:
            res = requests.post(url, headers=headers, data=data).json()

        else:
            res = requests.post(url,  data).json()
        return res

    # delete 请求方式
    def delete_req(self, url, data=None, headers=None):
        if headers is not None:
            res = requests.delete(url, data, headers).json()
        else:
            res = requests.delete(url, data).json()
        return res

    def main_req(self, method, url, data, headers):
        if method == "get":
            res = self.get_req(url, data, headers)
        elif method == 'post':
            res = self.post_req(url, data, headers)
        elif method == 'delete':
            res = self.delete_req(url, data, headers)
        else:
            res = "你的请求方式暂未开放，请耐心等待"
        return json.dumps(res, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == "__main__":
    ir = IntergrateRequest()
    # 测试获取所有文章
    # method = 'get'
    # url = 'http://127.0.0.1:8000/query/'
    # data = None
    # # headers = None
    # headers = {
    #         "X-Token": "96e79218965eb72c92a549dd5a330112"
    #     }
    # print(ir.main_req(method, url, data, headers))

    print('=================================')
    # res = requests.get('http://127.0.0.1:8000/query/', data=data, headers=headers)
    # print(type(res.json()))
    # a = res.json()
    #
    # print("test_query_article: ", a)
    # print("test_query_article: ", res.text)
    # 测试添加文章
    method = 'post'
    url = 'http://127.0.0.1:8000/articles/'
    # # data = {
    # #         "title": "孤舟蓑笠翁",
    # #         "content": "古朗月行",
    # #     }
    data = {
        "title": "sa224a",
        "content": "fafaaf",
    }
    headers = {
        # "Authorization": '通用的token，但是该接口使用的是X-Token',
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400",
        "X-Token": "96e79218965eb72c92a549dd5a330112"
    }
    print(ir.main_req(method, url, data, headers))



    print('-----------------------------------')
    # payload = {
    #     "title": "title777",
    #     "content": "content7777",
    # }
    # Headers = {
    #     # "Authorization": '通用的token，但是该接口使用的是X-Token',
    #     "Content-Type": "application/json; charset=utf-8",
    #     "Accept": "application/json",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400",
    #     "X-Token": "96e79218965eb72c92a549dd5a330112"
    # }
    # res = requests.post('http://127.0.0.1:8000/articles/', headers=Headers, json=payload)
    # print(res.request)
    # print(res.text)
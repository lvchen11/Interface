import json

import requests
import unittest


class TestInterfaceCrud(unittest.TestCase):
    # @unittest.skip("跳过 test_query_article 测试")
    def test_query_article(self):
        # payload = {}
        data = None
        headers = {
            "X-Token": "96e79218965eb72c92a549dd5a330112"
        }
        res = requests.get('http://127.0.0.1:8000/query/', data=data, headers=headers)
        print(type(res.json()))
        a = res.json()

        print("test_query_article: ", a)
        print("test_query_article: ", res.text)

    @unittest.skip("跳过 test_add_article 测试")
    def test_add_article(self):
        payload = {
            "title": "title5",
            "content": "content5",
        }
        Headers = {
            # "Authorization": '通用的token，但是该接口使用的是X-Token',
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400",
            "X-Token": "96e79218965eb72c92a549dd5a330112"
        }
        res = requests.post('http://127.0.0.1:8000/articles/', headers=Headers, json=payload)
        print(res.request)
        print(res.text)

    @unittest.skip("跳过 test_modify_article 测试")
    def test_modify_article(self):
        payload = {
            "title": "title1",
            "content": "content1",
        }
        Headers = {
            # "Authorization": '通用的token，但是该接口使用的是X-Token',
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400",
            "X-Token": "96e79218965eb72c92a549dd5a330112"
        }
        res = requests.post('http://127.0.0.1:8000/articles/1', headers=Headers, json=payload)
        print(res.request)
        print(res.text)

    @unittest.skip("跳过 test_delete_article 测试")
    def test_delete_article(self):
        payload = {
            "title": "title2",
            "content": "content2",
        }
        Headers = {
            # "Authorization": '通用的token，但是该接口使用的是X-Token',
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400",
            "X-Token": "96e79218965eb72c92a549dd5a330112"
        }
        res = requests.delete('http://127.0.0.1:8000/del_articles/1', headers=Headers, json=payload)
        print(res.request)
        print(res.text)

    @unittest.skip("跳过 test_test_api 测试")
    def test_test_api(self):
        payload = {
            'title': '春晓',
            'content': 'hffFajjjj',
            'status': 'alive'
        }
        res = requests.post('http://127.0.0.1:8000/test_api/')
        print(res.text)


if __name__ == '__main__':
    unittest.main()

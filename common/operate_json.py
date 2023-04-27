import json


class OperateJson(object):
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = '../operate_json.json'

        self.data = self.get_json()

    # 读取 json 文件
    def get_json(self):
        with open(self.file_name, encoding='utf-8') as fp:
            data = json.load(fp)
        return data
    # # 写入 json 文件
    # def write_json(self):
    #     with open(self.file_name, 'a', encoding='utf-8') as fp:
    #         data = json.dump(fp)
    #     return data

    # 根据关键词读取数据
    def get_key_data(self, key):
        return self.data[key]


if __name__ == '__main__':
    oj = OperateJson()
    print('login: ', oj.get_key_data("login"))
    print('login.username: ', oj.get_key_data("login")["username"])
    print('login.password: ', oj.get_key_data("login")["password"])
    print('logout: ', oj.get_key_data("logout"))
    print('logout.code: ', oj.get_key_data("logout")["code"])
    print('logout.info: ', oj.get_key_data("logout")["info"])
    
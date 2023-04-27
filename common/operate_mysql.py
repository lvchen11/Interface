import pymysql

class SwitchDatabase(object):

    def connect_databases(self):
        # 创建连接数据库的连接
        self.conn = pymysql.connect(
            host='172.172.30.53',
            user='root',
            password='123456',
            database='test',
            charset='utf8'
        )

        return self.conn

        # # 得到一个操作MySQL的光标对象
        # 默认执行完毕返回的结果集以元组显示
        # cursor_tuple = conn.cursor()
        # # 执行完毕返回的结果以字典显示
        # cursor_dict = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # # 执行sql
        # cursor_tuple.execute(sql)
        # # 关闭光标对象
        # cursor_tuple.close()
        # cursor_dict.close()
        # # 关闭数据库连接
        # conn.close()

    def close_databases(self):
        try:
            if self.conn:
                return self.conn.close()
        except Exception as e:
            print("Error: %s" % e)


if __name__ == "__main__":
    sql = """
        SELECT count(*) FROM test1
    """
    sd = SwitchDatabase()
    cursor = sd.connect_databases().cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    cursor.close()
    sd.close_databases()
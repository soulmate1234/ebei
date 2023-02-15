import pymysql
from camp_study_interface.aek.common.config_data import MYSQL_CONFIG


class MysqlDb:
    def __init__(self, host, port, user, password, db_name):

        self.db = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db_name
        )
        self.cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        self.cur.close()
        self.db.close()

    def select_db(self, sql):
        """查询"""
        try:
            self.cur.execute(sql)
            data = self.cur.fetchall()
            # 返回值这样[{'title': '标题2'}]  我想要这样 标题2
            # for k, v in data[0].items():
            #     return v
            return data
        except Exception as e:
            print("sql查询操作出现错误：{}".format(e))

    def execute_db(self, sql):
        """更新/插入/删除"""
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print("操作出现错误：{}".format(e))
            self.db.rollback()


mysql_db = MysqlDb(*MYSQL_CONFIG)

# if __name__ == '__main__':
#     print(mysql_db.select_db("SELECT * FROM employees"))
#     aa=3
#     mysql_db.execute_db(f"delete from user where id={aa}")

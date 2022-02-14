import pymysql
import json
import logging
from queue import Queue
from .zookeeper import Zookeeper
from .config import Config


class MysqlConnectPool:
    _mysql_queue = Queue()


    @staticmethod
    def init():
        for i in range(0, 4):
            db = Mysql()
            MysqlConnectPool._mysql_queue.put(db)

    @staticmethod
    def get_mysql_instance():
        instance = MysqlConnectPool._mysql_queue.get(block=True)
        return instance

    @staticmethod
    def back_mysql_instance(instance):
        MysqlConnectPool._mysql_queue.put(instance)

    @staticmethod
    def close():
        while not MysqlConnectPool._mysql_queue.empty():
            instance = MysqlConnectPool._mysql_queue.get(block=True)
            instance.close()

    @staticmethod
    def restart():
        logging.info("mysql restart")
        MysqlConnectPool.close()
        MysqlConnectPool.init()


class Mysql:

    def __init__(self):
        data_dict = {"host": Config.mysql_data['host'],"user": Config.mysql_data['user'], "password": Config.mysql_data['password']}
        v = json.dumps(data_dict)
        data = str.encode(v)
        try:
            data, _ = Zookeeper.zk.get("/mysql")
        except:
            logging.error("count't get mysql node")
        data_dict = json.loads(data)
        self.conn = pymysql.connect(host=str(data_dict['host']), user=str(data_dict['user']), password=str(data_dict['password']))
        logging.info("connect to mysql host:{}".format(data_dict['host']))
        self.cursor = self.conn.cursor()
        self._init_databases()
        self._init_tables()

    def _init_databases(self):
        create_db_sqls = []
        create_testdb_sql = "CREATE DATABASE IF NOT EXISTS {}".format(Config.mysql_data['database'])

        create_db_sqls.append(create_testdb_sql)
        for sql in create_db_sqls:
            self.cursor.execute(sql)

        use_testdb_sql = "USE test"
        self.cursor.execute(use_testdb_sql)

    def _init_tables(self):
        create_table_sqls = []
        create_bilibili_users_sql = "CREATE TABLE IF NOT EXISTS bilibili_users" \
                                    "(uid BIGINT PRIMARY KEY NOT NULL ," \
                                    "follower BIGINT ,following BIGINT ," \
                                    "archive BIGINT ,likes BIGINT ," \
                                    "vedios JSON)"

        create_table_sqls.append(create_bilibili_users_sql)
        for sql in create_table_sqls:
            self.cursor.execute(sql)

    def close(self):
        self.conn.close()


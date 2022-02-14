import json
import time
from center.zookeeper import Zookeeper
from center.controler import Controler
from task.bilibili_id import BilibiliIdTask
from public.zookeeper_operator import ZookeeperOperator
from center.connect_pool import MysqlConnectPool


class ZookeeperListener:

    @staticmethod
    def start():
        @Zookeeper.zk.DataWatch(Zookeeper.server_path)
        def watch_server_node(data, stat, event):
            status = 1
            message = {}
            try:
                ZookeeperOperator.lock(Zookeeper.lock_path)
                message = json.loads(data)
            except:
                ZookeeperOperator.unlock(Zookeeper.lock_path)
                status = 0
            if status == 1:
                thread_num = int(message['thread_num'])
                uid_begin = int(message['uid_begin'])
                uid_end = int(message['uid_end'])
                ZookeeperOperator.clear_node_value(Zookeeper.server_path)
                ZookeeperOperator.unlock(Zookeeper.lock_path)
                if thread_num != Controler.pool_size and thread_num != -1:
                    Controler.change_thread_pool_size(message['thread_num'])
                if uid_begin != -1 and uid_end != -1:
                    for uid in range(uid_begin, uid_end + 1):
                        task = BilibiliIdTask(uid)
                        Controler.add(task.run())

        @Zookeeper.zk.DataWatch('mysql')
        def watch_mysql_node(data, stat, event):
            MysqlConnectPool.restart()

        time.sleep(1e9)
 

import kazoo.client
from kazoo.client import KazooClient
from config import Config


class Zookeeper:
    zk = kazoo.client.KazooClient()
    server_root_path = "/server/"
    lock_root_path = "/lock/"
    mysql_path = "/mysql"

    @staticmethod
    def init():
        Zookeeper.zk = KazooClient(hosts=Config.zookeeper_data['host'])
        Zookeeper.zk.start()


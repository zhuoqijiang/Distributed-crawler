import kazoo.client
from kazoo.client import KazooClient
from .config import Config

class Zookeeper:
    zk = kazoo.client.KazooClient()
    server_path = ""
    lock_path = ""

    @staticmethod
    def init():
        Zookeeper.zk = KazooClient(hosts=Config.zookeeper_data['host'])
        Zookeeper.zk.start()
        path = "/server/"
        Zookeeper.server_path = Zookeeper.zk.create(path, b'', ephemeral=True, sequence=True, makepath=True)
        Zookeeper.lock_path = "/lock/" + Zookeeper.server_path[8:]


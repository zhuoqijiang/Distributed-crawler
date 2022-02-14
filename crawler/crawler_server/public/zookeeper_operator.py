import logging

from center.zookeeper import Zookeeper


class ZookeeperOperator:
    @staticmethod
    def create_esnode(path):
        while True:
            try:
                Zookeeper.zk.create(path, b'', ephemeral=True, makepath=True)
                return
            except:
                continue

    @staticmethod
    def delete_node(path):
        try:
            Zookeeper.zk.delete(path, recursive=True)
        except:
            logging.debug("delete node error")

    @staticmethod
    def clear_node_value(path):
            Zookeeper.zk.set(path, b'')

    @staticmethod
    def lock(path):
        ZookeeperOperator.create_esnode(path)

    @staticmethod
    def unlock(path):
        ZookeeperOperator.delete_node(path)

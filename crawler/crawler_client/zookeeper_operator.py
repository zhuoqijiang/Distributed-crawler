import logging

from zookeeper import Zookeeper


class ZookeeperOperator:

    @staticmethod
    def exists(path):
        result = Zookeeper.zk.exists(path)
        return result

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
        if ZookeeperOperator.exists(path):
                Zookeeper.zk.delete(path, recursive=True)

    @staticmethod
    def clear_node_value(path):
            Zookeeper.zk.set(path, b'')

    @staticmethod
    def lock(path):
        ZookeeperOperator.create_esnode(path)

    @staticmethod
    def unlock(path):
        ZookeeperOperator.delete_node(path)

    @staticmethod
    def get_child(path):
        child = []
        if ZookeeperOperator.exists(path):
            child = Zookeeper.zk.get_children(path)
        return child

    @staticmethod
    def set_node_value(path, value):
        if ZookeeperOperator.exists(path):
            Zookeeper.zk.set(path, value)

    @staticmethod
    def set_node_value_lock(lock_path, path, value):
        ZookeeperOperator.lock(lock_path)
        ZookeeperOperator.set_node_value(path, value)
        ZookeeperOperator.unlock(lock_path)

    @staticmethod
    def get_path(dst_child):
        lock_path = Zookeeper.lock_root_path + dst_child
        server_path = Zookeeper.server_root_path + dst_child
        return lock_path, server_path

import json

from zookeeper_operator import ZookeeperOperator
from zookeeper import Zookeeper
import random


class CmdHandler:
    @staticmethod
    def handle(cmd):
        cmd_list = cmd.split(' ')
        if len(cmd_list) < 1:
            return "命令错误"
        if cmd_list[0] == 'set':
            return CmdSetHandler.handle(cmd_list[1:])
        if cmd_list[0] == 'get':
            return CmdGetHandler.handle(cmd_list[1:])
        return "请输入 set 或者 get 关键字"


class CmdGetHandler:
    @staticmethod
    def handle(cmd_list):
        if len(cmd_list) < 1:
            return "无操作对象"
        if cmd_list[0] == "uid":
            return CmdGetHandler.UidHandler.handle(cmd_list[1:])
        if cmd_list[0] == "all":
            return CmdGetHandler.ServerHandler.handle(cmd_list[1:])
        return "操作对象错误"

    class UidHandler:
        @staticmethod
        def handle(cmd_list):
            if len(cmd_list) != 2:
                return "参数个数错误"
            first_arg = int(cmd_list[0])
            second_arg = int(cmd_list[1])
            if first_arg <= 0 or second_arg <= 0:
                return "uid值需大于0"
            if first_arg > second_arg:
                return "uid1需大于uid2"

            data_dict = {"uid_begin": cmd_list[0], "uid_end": cmd_list[1], "thread_num": "-1"}
            v = json.dumps(data_dict)
            value = str.encode(v)
            child = ZookeeperOperator.get_child(Zookeeper.server_root_path)
            dst_child = random.randint(0, len(child) - 1)
            lock_path, server_path = ZookeeperOperator.get_path(child[dst_child])
            ZookeeperOperator.set_node_value_lock(lock_path, server_path, value)

            return "success"

    class ServerHandler:
        @staticmethod
        def handle(cmd_list):
            if len(cmd_list) > 0:
                return "该命令参数为空"
            child = ZookeeperOperator.get_child(Zookeeper.server_root_path)
            childstr = ",".join(child)
            return childstr


class CmdSetHandler:
    @staticmethod
    def handle(cmd_list):
        if len(cmd_list) < 1:
            return "无操作对象"
        if cmd_list[0] == "mysql":
            return CmdSetHandler.MysqlHandler.handle(cmd_list[1:])
        if cmd_list[0] == "thread":
            return CmdSetHandler.ThreadNumHandler.handle(cmd_list[1:])

    class ThreadNumHandler:

        @staticmethod
        def handle(cmd_list):
            if len(cmd_list) > 2 or len(cmd_list) < 1:
                return "参数个数错误"
            thread_num = 0
            dst = ""
            child = ZookeeperOperator.get_child(Zookeeper.server_root_path)
            if len(cmd_list) == 2:
                thread_num = int(cmd_list[1])
                dst = cmd_list[0]
            if len(cmd_list) == 1:
                thread_num = int(cmd_list[0])
                dst = child[0]
            if thread_num < 1:
                return "线程数需大于0"
            data_dict = {"uid_begin": "-1", "uid_end": "-1", "thread_num": thread_num}
            v = json.dumps(data_dict)
            value = str.encode(v)
            lock_path, server_path = ZookeeperOperator.get_path(dst)
            ZookeeperOperator.set_node_value_lock(lock_path, server_path, value)

            return "success"

    class MysqlHandler:
        @staticmethod
        def handle(cmd_list):
            if len(cmd_list) != 3:
                return "参数个数错误"
            data_dict = {"host": cmd_list[0], "user": cmd_list[1], "password": cmd_list[2]}
            v = json.dumps(data_dict)
            value = str.encode(v)
            ZookeeperOperator.set_node_value(Zookeeper.mysql_path, value)
            return "success"

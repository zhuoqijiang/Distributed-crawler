from center.global_register import Global
from listener.zookeeper_listener import ZookeeperListener


def main():
    Global.init()
    ZookeeperListener.start()


if __name__ == '__main__':
    main()









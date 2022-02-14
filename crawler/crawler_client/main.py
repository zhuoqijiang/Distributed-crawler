import time

from cmd_listener import CmdListener
from zookeeper import Zookeeper
from config import Config


def main():
    Config.init()
    Zookeeper.init()
    CmdListener.start()


if __name__ == '__main__':
    main()



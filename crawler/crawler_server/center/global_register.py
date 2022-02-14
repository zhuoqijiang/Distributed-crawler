import logging
from .connect_pool import MysqlConnectPool
from .controler import Controler
from .zookeeper import Zookeeper
from .config import Config


class Global:
    @staticmethod
    def init():
        logging.basicConfig(filename='./Logout.log', format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                            level=logging.INFO)
        Config.init()
        Zookeeper.init()
        Controler.init()
        MysqlConnectPool.init()
        logging.info("init successfully")

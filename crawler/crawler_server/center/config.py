import yaml


class Config:
    data = {}
    mysql_data = {}
    zookeeper_data = {}

    @staticmethod
    def init():
        fs = open("config.yaml", encoding="UTF-8")
        Config.data = yaml.load(fs, Loader=yaml.FullLoader)
        Config.mysql_data = Config.data['mysql']
        Config.zookeeper_data = Config.data['zookeeper']

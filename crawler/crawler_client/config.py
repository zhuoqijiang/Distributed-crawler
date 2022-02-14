import yaml


class Config:
    data = {}
    zookeeper_data = {}
    @staticmethod
    def init():
        fs = open("config.yaml", encoding="UTF-8")
        Config.data = yaml.load(fs, Loader=yaml.FullLoader)
        Config.zookeeper_data = Config.data['zookeeper']

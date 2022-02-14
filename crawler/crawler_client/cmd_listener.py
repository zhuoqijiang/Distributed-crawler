from cmd_handler import CmdHandler

class CmdListener:
    @staticmethod
    def start():
        while True:
            cmd = input("请输入命令:")
            if not len(cmd):
                continue
            try:
                response = CmdHandler.handle(cmd)
            except:
                response = "error"
            print(response)

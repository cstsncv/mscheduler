from .config import MASTERURL
from .cm import ConnectionManager
import zerorpc  #zerorpc内操作不允许放至线程中运行

class Master:
    def __init__(self):
        self.server = zerorpc.Server(ConnectionManager())

    def start(self):
        self.server.bind(MASTERURL)
        self.server.run()

    def shutdown(self):
        self.server.close()



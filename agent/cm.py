import zerorpc
import threading
from .config import CONNECTIONURL




class ConnectionManage:
    def __init__(self):
        self.client = zerorpc.Client()
        self.event = threading.Event()

    def  start(self,timeout=None):
        self.client.connect(CONNECTIONURL)  #建立连接
        while not self.event.wait(timeout):
            pass

    def shutdown(self):
        self.event.set()
        self.client.close()








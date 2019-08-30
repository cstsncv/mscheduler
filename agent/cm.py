import zerorpc
import threading
from .config import CONNECTIONURL
from . utils import getlogger
from . msg import Message

logger = getlogger(__name__, 'd:/agent.cm.log')

class ConnectionManage:
    def __init__(self):
        self.client = zerorpc.Client()
        self.event = threading.Event()
        self.message = Message('d:/myid')

    def start(self,timeout=5):
        try:
            self.event.clear()
            self.client.connect(CONNECTIONURL)  #建立连接
            rex = self.message.reg()
            logger.info(self.client.sendmsg(rex))
            while not self.event.wait(timeout):
                logger.info(self.client.sendmsg(self.message.heartbeat()))
        except Exception as e:
            logger.error("{}".format(e))
            raise e
    def shutdown(self):
        self.event.set()
        self.client.close()

    def join(self):
        self.event.wait()






#程序执行,返回结果状态码和程序运行结果

from subprocess import Popen, PIPE
from .utils import getlogger

logger = getlogger(__name__,'d:/exec.log')


class Executor:
    # def __init__(self, script, timeout=None):
    #     self.script = script
    #     self.timeout = timeout

    def run(self, script, timeout=None):
        proc = Popen(script, shell=True, stdout=PIPE)
        code = proc.wait(timeout)
        txt = proc.stdout.read()
        logger.info("return code:{}, txt: {}".format(code, txt))
        # print(code, txt)
        return code, txt


 #e = Executor('echo "asdasdas"')
# e = Executor('ipconfig /all1')
# p = e.run()
# print(p[0],p[1].decode('gbk'))










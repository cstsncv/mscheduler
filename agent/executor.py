#程序执行

from subprocess import Popen, PIPE

class Executor:
    def __init__(self, script, timeout=None):
        self.script = script
        self.timeout = timeout

    def run(self):
        proc = Popen(self.script, shell=True, stdout=PIPE)
        code = proc.wait(self.timeout)
        txt = proc.stdout.read()
        # print(code, txt)
        return code, txt


# e = Executor('echo "asdasdas"')
# print(e.run())










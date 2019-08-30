import subprocess
from subprocess import Popen, PIPE
import zerorpc
import threading

client = zerorpc.Client()
client.connect('tcp://127.0.0.1:9000')

e =threading.Event()

while True:
    res = client.hello('asdasd')
    print(res)
    print("~"*50)
    e.wait(3)

client.close()



proc = Popen('echo "hello"', shell=True, stdout=PIPE)
code = proc.wait()
print(code)

txt = proc.stdout.read()
print(txt)
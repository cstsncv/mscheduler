
import zerorpc

MASTERURL = "tcp://0.0.0.0:9000"

class Master:

    def hello(self, msg):
        #return 'hello zerorpc {}'.format(msg)
        return '{"a":1,"b":{"c":2,"d":3},"e":4}'


server = zerorpc.Server(Master())
server.bind(MASTERURL)
server.run()
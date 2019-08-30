
import zerorpc  #zerorpc内操作不允许放至线程中运行

MASTERURL = "tcp://0.0.0.0:9000"

agents = {}
class Master:

    def handle(self, msg):
        print(msg,type(msg))
        #if msg['type'] == "register" or msg["type"] == 'heartbeat':
        if msg['type'] in {'register', 'heartbeat'}:
            agents[msg['payload']['id']] = msg['payload']['hostnme'], msg['payload']['ip']
        print(agents)
        return ' ack {}'.format(msg)
        #return '{"a":1,"b":{"c":2,"d":3},"e":4}'

    sendmsg = handle

server = zerorpc.Server(Master())
server.bind(MASTERURL)
server.run()
from .storage import Storage


class ConnectionManager:
    def __init__(self):
        self.store = Storage()
    def handle(self, msg):
        print(msg,type(msg))
        #if msg['type'] == "register" or msg["type"] == 'heartbeat':
        if msg['type'] in {'register', 'heartbeat'}:
            self.store.agents[msg['payload']['id']] = msg['payload']['hostname'], msg['payload']['ip']
        print(self.store.agents)
        return ' ack {}'.format(msg)
        #return '{"a":1,"b":{"c":2,"d":3},"e":4}'

    sendmsg = handle

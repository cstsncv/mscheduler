from .storage import Storage

"""
handle_msg = {
            "type": "register",
            "payload": {
                "id": self.id,
                "hostname": socket.gethostname(),
                "ip": self.get_addresses()
                }
        }
"""
class ConnectionManager:
    def __init__(self):
        self.store = Storage()
    def handle(self, msg):
        #print(msg,type(msg))
        #if msg['type'] == "register" or msg["type"] == 'heartbeat':
        try:
            if msg['type'] in {'register', 'heartbeat'}:
                self.store.reg_hb(**msg['payload'])
            elif msg['type'] == "result":
                self.store.result(msg['payload'])

            print(self.store.get_agents())
            return ' ack {}'.format(msg)
            #return '{"a":1,"b":{"c":2,"d":3},"e":4}'
        except Exception as e:
            pass
    sendmsg = handle

    def add_task(self, msg: dict):
        return self.store.add_task(msg)

    def get_task(self, agent_id):
        return self.store.get_task(agent_id)

    def get_agents(self):
        return self.store.get_agents()





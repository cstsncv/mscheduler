import uuid
import socket
import netifaces
import ipaddress
import  os

class Message:
    def __init__(self,myidpath):
        if os.path.exists(myidpath):
            with open(myidpath) as f:
                self.id = f.readline().strip()
        else:
            self.id = uuid.uuid4().hex
            with open(myidpath, 'w') as f:
                f.write(self.id)
        print(self.id)
    def get_addresses(self):  #获取本机IP列表
        addresses = []
        ifaces = netifaces.interfaces()
        for iface in ifaces:
            ips = netifaces.ifaddresses(iface)
            # print(ips)
            if 2 in ips:
                for ip in ips[2]:
                    address = ipaddress.ip_address(ip['addr'])
                    if address.is_link_local or address.is_loopback or address.is_loopback \
                            or address.is_reserved:
                        continue
                    addresses.append(str(address))
        return addresses

    def reg(self, ):
        #生成注册信息
        return {
            "type": "register",
            "payload": {
                "id": self.id,
                "hostname": socket.gethostname(),
                "ip": self.get_addresses()
                }
        }

    def heartbeat(self):
        return {
            "type": "heartbeat",
            "payload": {
                "id": self.id,
                "hostname": socket.gethostname(),
                "ip": self.get_addresses()
                }
        }

    def result(self, task_id, code, output):  #返回给master的执行结果信息
        return {
            "type": "result",
            "payload": {
                "agent_id": self.id,
                "id": task_id,
                "code": code,
                "output": output
            }
        }






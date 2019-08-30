import netifaces
import ipaddress
from agent import Agent

if __name__ == "__main__":
    agent = Agent()
    try:
        agent.start()
    except Exception as e:
        agent.shutdown()


# ifaces = netifaces.interfaces()
# #print(ifaces)
#
# addresses = []
#
# for iface in ifaces:
#     ips = netifaces.ifaddresses(iface)
#     # print(ips)
#     if 2 in ips:
#         for ip in ips[2]:
#             address = ipaddress.ip_address(ip['addr'])
#             if address.is_link_local or address.is_loopback or address.is_loopback \
#                 or address.is_reserved:
#                 continue
#             addresses.append(address)
#             print(addresses)
# proc = Popen('echo "hello"', shell=True, stdout=PIPE)
# code = proc.wait()
# print(code)
#
# txt = proc.stdout.read()
# print(txt)
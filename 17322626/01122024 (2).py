#2231
from ipaddress import *
net4 = list(ip_network('162.198.0.157/255.255.255.224',0))
a=0
print(net4)
for x in net4:
    a+=1
    print (f"{bin(int(x))[2:]},{x},{a}")
    s=bin(int(x))[2:]
for i in range(23,24):
    subnet1=ip_network(f"172.16.168.0/{i}", 0)
for i in range(32,0,-1):
    subnet1=ip_network(f"255.255.248.0/{i}",0)
q = 0
for x in subnet1:
    q +=1
    print(x)
    print(q)
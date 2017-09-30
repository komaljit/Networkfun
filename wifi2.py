import socket
import os
from threading import Thread
j=1
def check(p,t):
    response=os.popen(p)
    for line in response.readlines():
        if line.count("TTL"):     
            print(t+" is connected")         
        else:
            pass

s="10.0.0."

for i in range (1,255):
    m=s+str(i)
    p="ping -n 1 "+m
    k=Thread(target=check,args=(p,m,))
    k.start()
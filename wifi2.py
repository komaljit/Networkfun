import socket
import os
from threading import Thread
# A simple program to check the IP addreses connected to your home or office router.

def check(p,t):
    response=os.popen(p)
    for line in response.readlines():
        if line.count("TTL"):     
            print(t+" is connected")         
        else:
            pass
# The IP address range of my router is 10.0.0.0/24 (private subnet). I am changing only the fourth octet. You can change the range as you wish. 

s="10.0.0."
for i in range (1,255):
    m=s+str(i)
    p="ping -n 1 "+m
    k=Thread(target=check,args=(p,m,))
    k.start()

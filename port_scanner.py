import socket
from threading import Thread
import time


def check(st,en):
    a="10.0.0.1"
    for i in range(st,en+1):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        try:
            s.connect((a,i))
            print("connected on port "+str(i))
            sock.close()
           
        except:   
            pass
st=1
i=655
for j in range(1,int(i)+1):
    en=st+100
    y=Thread(target=check,args=(st,en,))
    y.start()
    st=st+100 
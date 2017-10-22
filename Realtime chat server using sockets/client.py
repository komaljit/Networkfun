import socket
import sys
import select
import datetime


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)      
try:
    s.bind(("127.0.0.1",int(sys.argv[1])))
except Exception:
    print("Port already in use")
    sys.exit()
s.connect(("localhost",2000))
while True:
    reader,_,_ = select.select([s,sys.stdin],[],[])
    for i in reader:
        if i is s:
            mes = s.recv(1024)
            if mes:
                d = datetime.datetime.now()
                print("{}-{}-{}: ".format(d.month,d.day,d.year)+mes.decode("utf-8"))
        else:
            data = sys.stdin.readline()
            s.send(data.encode("utf-8")) 

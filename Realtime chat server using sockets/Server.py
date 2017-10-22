import socket
import select
import sys
import time

class chatapp:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(("127.0.0.1",2000))
        self.socket.listen(10)
      
    def broadcast(self,message,sender):
        for i in self.list1[1:]: 
            if i == sender:
                continue
            try:          
                i.send(message.encode("utf-8"))
            except: 
                i.close()
                self.list1.remove(i)
                
    def ma(self):
        self.list1=[self.socket]
        while True:            
            self.read,_,_ = select.select(self.list1,[],[])
            for i in self.read:
                if i is self.socket:
                    self.conn,self.add = self.socket.accept()
                    self.list1.append(self.conn)
                    self.data = "Welcome to the party "+str(self.add)
                    self.conn.send(self.data.encode("utf-8"))
                    self.data = str(self.add) + " has joined the party"
                    self.broadcast(self.data,self.conn)                       
                else:                                     
                    self.data = i.recv(1024)
                    if self.data:                   
                        self.broadcast(self.data,i) 
       

d=chatapp()
d.ma()
sys.exit()

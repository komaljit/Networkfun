
import socket
import os
import sys
s=socket.socket()
a="localhost"
port=5555
s.bind((a,port))
s.listen(5)

while True:
    conn, add = s.accept()
    file_name=conn.recv(1024).decode("utf-8")
    if os.path.isfile(file_name):
        response_code=str(200)
        conn.send(response_code.encode())
        size=str(os.path.getsize(file_name))
        conn.send(size.encode())
        response=conn.recv(1024).decode("utf-8")        
        if response=="Y":
                print(response+ " 1")
                with open(file_name,"rb")as f:
                    bytestosend=f.read(1024)
                    conn.send(bytestosend)
                    len=0
                    while len<int(size):
                        len=len+1024
                        bytestosend=f.read()
                        conn.send(bytestosend) 
                    conn.send("File download complete".encode())
    else:
        response_code=str(404)
        conn.send(response_code.encode())

    sys.exit()


           
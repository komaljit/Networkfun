import socket
import sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 5555
a = "localhost"
s.connect((a,port))


while True:  
    file_name = input("> Enter the file path you wish to download- ")
    s.send(file_name.encode())  
    response = s.recv(1024).decode("utf-8")
    if response == "404":
        print("File does not exists")
        continue
    elif response == "200":
        file_size = s.recv(1024).decode("utf-8")
        print("File size is ",file_size)
        r = input("> Do you wish to download? Enter Y or N").upper()
        if r == "Y":
            s.send(r.encode("utf-8"))
            download = s.recv(1024)
            f = open("C:/Users/Komal Raju/yipee","wb+")
            len = 0
            while len<int(file_size):
                len = len+1024
                f.write(download)
            print(s.recv(1024).decode())
            break
        elif r == "N":
            break

sys.exit()
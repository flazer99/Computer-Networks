import socket

s = socket.socket()
port = 3000
s.bind(('',port))
s.listen(5)
file = open("data.txt","r")
data = file.read()
print("Socket created and listening !")
while True:
    c, addr = s.accept()
    print("Connection established with ",addr)
    c.send(bytes(str(data),"utf-8"))
        
    file2 = open('LogFile1',"r")
    proc = file2.read()
    print(proc)
c.close()

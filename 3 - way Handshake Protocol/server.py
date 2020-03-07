import socket 
import random 

s = socket.socket()
s.bind(('',3000))
s.listen(5)

forward = dict()
ind = 0

while True:
    c, addr = s.accept()
    if(c not in forward.values()):
        forward[ind] = c
        ind+=1
    print("Connected to the client ",c)
    c.send(bytes("200","utf-8"))
    
    data = c.recv(1024).decode("utf-8")
    print(data)
    segment = data.split()
    print("Recieved SYN packet from the client")
    print("SYN :- ", segment[0]," Segment# :- ",segment[2])
          
    segment[2] = int(segment[2]) + 1
    segment[1] = int(segment[1]) + 1
    message = ""
    for i in segment:
        message += str(i) + " "
    c.send(bytes(str(message),"utf-8"))
    
    data = c.recv(1024).decode("utf-8")
    segment = data.split()
    print("Recieved from the client")
    print("SYN :- ", segment[1]," Segment# :- ",segment[2])
          
    print("3-way handshake is successful with the client!")
    
    print("Add more clients? Y/N")
    x = input()
    if(x=='y' or x=='Y'):
        continue
    else:
        break
    
        
    
    
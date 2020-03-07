import socket
import random

s = socket.socket()
s.connect(('127.0.0.1',3000))

while True:
    conf = s.recv(1024).decode("utf-8")
    if(conf == "200"):
        print("Connected to the Client!")
        print("Do you want to request for some data form the server? Y/N")
        x = input()
        if(x=='Y' or x=='y'):
            r1 = random.randint(0,1000)
            message = "1 0 "+str(r1)
            s.send(bytes(str(message),"utf-8"))
            
            data = s.recv(1024).decode("utf-8")
            segment = data.split()
            print("Received SYN-ACK from the server")
            print("SYN :- ", segment[0]," ACK :- ",segment[1]," Segment# :- ",segment[2])
                  
            r1 = random.randint(0,1000)
            message = "0 1 "+str(r1)
            s.send(bytes(str(message),"utf-8"))
            
            print("Congrats on getting connected!")
            break
        
    
            
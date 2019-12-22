import socket
s = socket.socket()
s.connect(('127.0.0.1',3000))
while True:
    conf = s.recv(1024).decode("utf-8")
    if(conf == "200"):
        print("Successful Connection ! ")
        print("Do you want to send message to a client ? y/n ")
        x = input()
        if(x=="y" or x=="Y"):
            s.send(bytes(x,"utf-8"))
            print(s.recv(1024).decode("utf-8"))
            client = input()
            s.send(bytes(str(client),"utf-8"))
            print(s.recv(1024).decode("utf-8"))
            msg = input()
            s.send(bytes(str(msg),"utf-8"))
            print(s.recv(1024).decode("utf-8"))
        else:
            print(s.recv(1024).decode("utf-8"))
            
        

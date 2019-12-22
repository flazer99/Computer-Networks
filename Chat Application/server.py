import socket
s = socket.socket()
s.bind(('',3000))
s.listen(5)
forward = {}
it = 0
ch = ""
while (ch!="n" and ch!="N"):
    c, addr = s.accept()
    if(c not in forward.values()):
        forward[it] = c
        it+=1
    c.send(bytes("200","utf-8"))
    print("Do you want to add more clients? Y/N ")
    ch = input()
    
print("Exiting while for adding clients ")  

while True:
    for i in forward:
        trans = forward[i].recv(1024).decode("utf-8")
        if( trans == "y" or trans == "Y" ):
            forward[i].send(bytes("Client# :- ","utf-8"))
            client = forward[i].recv(1024).decode("utf-8")
            forward[i].send(bytes("Type your message for the client :- ","utf-8"))
            msg = forward[i].recv(1024).decode("utf-8")
            forward[int(client)].send(bytes(str(msg),"utf-8"))
            forward[i].send(bytes("Message sent to the specified client! ","utf-8"))
    
    
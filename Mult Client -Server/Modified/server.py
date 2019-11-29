import socket

s = socket.socket()
port = 3000
s.bind(('',port))
s.listen(5)
print("Socket created and listening !")
li = []
address = []
s_items = ['Hey','Broke','This','Up','Well']

while True:
    c, addr = s.accept()
    if(c not in li):
        li.append(c)
    if(addr not in address):
        address.append(addr)
    print("Connection established with ",addr)
    print("Send Data type to client")
    str1 = input()
    c.send(bytes(str1,"utf-8"))
    data = c.recv(1024).decode("utf-8")
    
    print(data)
    if(data == "200"):
        print("File has been succesfully initialized by the client")
        file = open("data.txt","r")
        value = file.read().split("\n")
        print(value)
        
    else:
        print("Recieved from the client - ",data)
    
    print('Forwarding Table')
    print(li)
    print("List of connections at the server")
    print(address)
    
    print("Do you want to continue Y/N")
    ch = input()
    if(ch == 'n'or ch == 'N'):
        break

send = 0
i = 0
inc = len(value)//len(address)
j = 0
print(value)
sb = " "
for i in li:
    print("for loop, increment value ", inc," length of value ",len(value)," length of address ",len(address))
    ctr = 0
    for k in range(inc):
        sb = sb + " " + value[j+k]  
    i.send(bytes(str(sb),"utf-8"))
    ctr+=1
    j+=inc
c.close()

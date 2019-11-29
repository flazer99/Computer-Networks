import socket

s = socket.socket()
port = 3000
s.connect(('127.0.0.1',port))
print("Recieved :-")
temp = ""
while True:
    
    data = s.recv(1024).decode("utf-8")
    if(temp is not data):
        temp = data
    print(temp)
    print("Do you want to create a file Y/N?")
    ch = input()
    
    if(ch == 'y' or ch == 'Y'):
        ch = ""
        file = open("data.txt","a")
        print("Enter contents line by line")
        while(ch!='y' and ch!='Y'):
            line = input()
            file.write(line)
            print("Do you want to stop Y/N?")
            ch = input()
            s.send(bytes("200","utf-8"))
    else:
        print("Enter input from the client : ")
        str1 = input()
        s.send(bytes(str1,"utf-8"))
s.close()


    
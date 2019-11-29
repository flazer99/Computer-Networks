# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:58:20 2019

@author: axelb
"""

import socket
import random
import string
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
        
        if(temp == "int"):
            print("Enter the number of integer values")
            x = int(input())
            for i in range(x):
                res = random.randint(0,10)
                file.write(str(res) + "\n")
        
        elif(temp  == "float"):
            print("Enter the number of float values")
            x = int(input())
            for i in range(x):
                res = random.random()
                file.write(str(res)+"\n")
        
        elif(temp == "string"):
            print("Enter the number of strings")
            x = int(input())
            for i in range(x):
                res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))
                file.write(str(res) + "\n")
            
        elif(temp == "boolean"):
            print("Enter a boolean value")
        file.close()
        s.send(bytes("200","utf-8"))
    else:
        print("Enter input from the client : ")
        str1 = input()
        s.send(bytes(str1,"utf-8"))
s.close()


    
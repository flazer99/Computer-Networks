# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 01:07:03 2019

@author: axelb
"""

import socket
from _thread import *
import threading

def thread(c):
    while True:
        trans = c.recv(1024).decode("utf-8")
        if( trans == "y" or trans == "Y" ):
            c.send(bytes("Client# :- ","utf-8"))
            client = c.recv(1024).decode("utf-8")
            c.send(bytes("Type your message for the client :- ","utf-8"))
            msg = c.recv(1024).decode("utf-8")
            forward[int(client)].send(bytes(str(msg),"utf-8"))
            c.send(bytes("Message sent to the specified client! ","utf-8"))


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
    start_new_thread(thread, (c,)) 
    print("Do you want to add more clients? Y/N ")
    ch = input()
    
print("Exiting while for adding clients ")  

        
    
    
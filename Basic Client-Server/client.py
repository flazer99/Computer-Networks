import socket

s = socket.socket()
port = 3000
s.connect(('127.0.0.1',port))
print("Recieved :-")
data = s.recv(1024).decode("utf-8")
data = data.split("\n")
for i in range(len(data)):
    data[i] = data[i].split(' ')
dict = {}
loss = 0
trp = 0

#Writing to file
file = open('LogFile3','x')
file.write('Packet Loss      Through Put')
print("Packet Loss      Through Put")

for i in data:
  #  print(i)
    loss = int(i[2])-int(i[3])
    trp = int(i[3])/int(i[2])
    if(i[0] in dict):
        dict[i[0]] += 1
    else:
        dict[i[0]] = 1
    print(loss,"                ",trp)
    temp_str = str(loss)+"                "+str(trp)
    file.write(temp_str)
avg = 0

for i in dict:
    avg = dict[i]/3
    print("No of transmissions :- ",dict[i], " Average transmissions:- ",avg)

#print(data)
#print(dict)

x = input("Enter the Source IP")
print("No of transmissions :- ",dict[x], " Average Transmissions :- ",dict[x]/3)
s.close()



import socket,time
host='localhost'
port=50007
s=socket.socket()
s.connect((host,port))
# s.recv(1024)
pass2 = raw_input("Enter password")
s.send(pass2)
print s.recv(1024)
query = raw_input("")
s.send(query)
qdata = s.recv(1024)
print qdata
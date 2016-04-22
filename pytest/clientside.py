import socket,time
host='localhost'
port=50007
s=socket.socket()
s.connect((host,port))
data=s.recv(4096)
print data
ch=input('Enter choice')
print type(ch)
s.send(str(ch))
print s.recv(4096)

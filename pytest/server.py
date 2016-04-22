import socket
from collections import deque

s=socket.socket()

message=""
host=socket.gethostname()
port=12345

s.bind((host,port))

s.listen(5)
while True:
	c,addr=s.accept()
	msg='Got connection from' + str(addr)
	print msg
	message=message+msg
	c.send('Thank You for Connecting')
	str1=c.recv(4096)
	msg1= 'recieved the string :' +str(str1)
	print msg1
	message=message+'\n'
	message=message+msg1
	q1=deque()
	q=deque(str1)
	for l in q:
		if l=='*':
			q1.pop()
		else:
			if l!=' ':
				q1.appendleft(l)
	print q1
	c.send(str(deque(q1)))
	c.close()

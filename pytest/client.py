import socket

s=socket.socket()

message=""
host=socket.gethostname()
port=12345

s.connect((host,port))
msg=s.recv(4096)
print msg
message=message+msg
str1=raw_input("Enter a String of atleast 26 characters")

s.send(str1)
msg1=s.recv(4096)
print msg1
message=message+"\n"
message=message+msg1

print message
s.close




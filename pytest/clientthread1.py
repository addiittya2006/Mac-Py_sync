import socket,time
host='localhost'
port=50007
s=socket.socket()
s.connect((host,port))
while True:
    time.sleep(10)
    s.send("Hai")

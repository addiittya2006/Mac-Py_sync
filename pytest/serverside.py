import socket,thread
host=''
port=50007
s=socket.socket()
s.bind((host,port))
s.listen(5)
def handleclient(conn,addr):
  
    ch=conn.recv(4096)
    ch=str(ch)
    if ch=='1':
	conn.send("Enter Path")
while True:
    conn,addr=s.accept()
    print 'connected to ',addr
    thread.start_new_thread(handleclient,(conn,addr))

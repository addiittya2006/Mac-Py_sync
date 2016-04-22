import socket,thread
host=''
port=50007
s=socket.socket()
s.bind((host,port))
s.listen(5)
def handleclient(conn):
    while True:
        data=conn.recv(7)
        print data
        if not data:
            break
while True:
    conn,addr=s.accept()
    print 'connected to ',addr
    thread.start_new_thread(handleclient,(conn,))


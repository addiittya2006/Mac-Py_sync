import socket,thread,time
host=''
port=50007
s=socket.socket()
s.bind((host,port))
s.listen(5)


fileob = open("database.data","r")
list1=[]
list2=[]

for line in fileob.readline():
	q = line.split(" ")
	for i in q:
		list2.append(q)
	list1.append(list2)

fileob.close()

def handleclient(conn):
    while True:
    	# conn.send("Enter Password.")
        # time.sleep(20)
        data=conn.recv(20)
        # print data
    	print data,type(data),len(data)
        # print data1

        if data == "password":
        	conn.send("you are connected\nEnter Item No.")
        	query = conn.recv(10)
        	query1 = str(query)
        	for line in list1:
        		if str(line[0]) == query:
        			conn.send(line[1]+" >> "+line[2]+" >> "+line[3])
        		else:
        		 	print "Value does not exist."

        if not data:
            break
while True:
    conn,addr=s.accept()
    print 'connected to ',addr
    thread.start_new_thread(handleclient,(conn,))
import socket
import time
from Tkinter import *

BUFFER_SIZE = 1024
TCP_IP = 'localhost'
TCP_PORT = 1235

def send():
    print 'send'

# def recv():
    # print 'recv'

def printAnswer(clientSock):
    print "Recieve: "
    data = clientSock.recv(BUFFER_SIZE)
    print "Data Recieved: ", data
    if len(data) == 0:
        print "no response!"


def main():

    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSock.bind((TCP_IP, TCP_PORT))
    serverSock.listen(1)

    try:
      while True:
          print "\n\nConnection on Port " + str(TCP_PORT)
          clientSock, address = serverSock.accept()
          print "Client conected " + str(address)
          # clientSock.send("Hello PythonServer!")
          # while True:
                # data = clientSock.recv(BUFFER_SIZE)
                # if not data or data=='q':
                    # break
                # sys.stdout.write(data.decode('utf-8')+' ')
                # clientSock.send(data.encode('utf-8'))
          print clientSock.recv(BUFFER_SIZE)
          clientSock.send("Menu\n1.1. Print the elements in reverse order.\n2. Sort the elements in the list.\n")
          print clientSock.recv(BUFFER_SIZE)

          clientSock.close()
          print "\nClient offline:" + str(address)
    finally:
        serverSock.close()

    # print "Starting Client"
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print "Conecting.."
    clientSock.connect((TCP_IP, TCP_PORT))
    time.sleep(1)
    printAnswer(clientSock)
    # while True:
        # message=raw_input("Enter Message");
    message = str(sendarray.get())
    clientSock.send(message.decode(sys.stdin.encoding).encode('utf-8'))
    # time.sleep(1)
    printAnswer(clientSock)
    clientSock.close()


root = Tk()
Label(root,text="Enter Numbers").grid(row=0)

send_array = StringVar()
sendarray = Entry(root, textvariable = send_array)
sendarray.grid(row=0, column=2)

# number_of_out_intrf = StringVar()
# entry_no_interface = Entry(root, textvariable = number_of_out_intrf)
# entry_no_interface.grid(row=1, column=1)
b = Button(root,text="Send!", command=main)
b.grid(row=0,column=3)

textField = Text(root)
textField.grid(row=1,columnspan=4)
root.mainloop()
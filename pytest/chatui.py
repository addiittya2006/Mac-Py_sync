import socket
import time
import sys
from Tkinter import *

BUFFER_SIZE = 1024
TCP_IP = 'localhost'
TCP_PORT = 12355

# def send():
#     print 'send'

# def recv():
    # print 'recv'

def printAnswer(clientSock):
    # print "Recieve: "
    data = clientSock.recv(BUFFER_SIZE)
    print "Data Recieved: ", data
    # textField.set
    if len(data) == 0:
        print "no response!"


# def wait(seconds):
#     print "Wait "+str(seconds)
#     time.sleep(seconds)


def main():
    print "Starting Client"
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Conecting.."
    clientSock.connect((TCP_IP, TCP_PORT))
    # printAnswer(clientSock)
    message = str(sendarray.get())
    clientSock.send(message)
    time.sleep(1)
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
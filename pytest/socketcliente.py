import socket
import time
import sys

BUFFER_SIZE = 1024
TCP_IP = 'localhost'
TCP_PORT = 1235


def printAnswer(clientSock):
    print "Recieve: "
    data = clientSock.recv(BUFFER_SIZE)
    print "Data Recieved: ", data
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
    time.sleep(1)
    printAnswer(clientSock)
    while True:        
        message=raw_input("Enter Message: ");
        clientSock.send(message.decode(sys.stdin.encoding).encode('utf-8'))
        wait(1)
        printAnswer(clientSock)
    clientSock.close()
        

if __name__ == "__main__":
    main()

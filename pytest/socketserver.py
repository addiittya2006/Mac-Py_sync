import socket
import sys

BUFFER_SIZE = 1024
TCP_IP = 'localhost'
TCP_PORT = 12355

def main():


    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSock.bind((TCP_IP, TCP_PORT))
    serverSock.listen(1)

    try:
        while True:
            print "\n\nConnection on Port " + str(TCP_PORT)
            clientSock, address = serverSock.accept()
            print "Client conected: " + str(address)
            # clientSock.send("Hello PythonServer!")
            # while True:
            data = clientSock.recv(BUFFER_SIZE)
            # if not data or data=='q':
            #     break
            # sys.stdout.write(data.decode('utf-8')+' ')
            p = []
            # m = str(data)
            m = data.split(',')
            # print m

            for i in m:
                p.append(int(i))

            mo = ''.join(str(e) for e in sorted(p))

            lo = reversed(data)

            data1 = str(p.reverse())+'    fhdsgxc   '+mo

            clientSock.send(data1.encode('utf-8'))

            # clientSock.send("Goodbye.")
            clientSock.close()
            # print "\nClient offline:" + str(address)
    finally:
        serverSock.close()

if __name__ == "__main__":
    main()

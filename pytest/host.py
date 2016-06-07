import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

server_socket.bind((host, port))

server_socket.listen(5)

while True:
    # establish a connection
    client_socket = server_socket.accept()

    # print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    client_socket.send(currentTime.encode('ascii'))
    client_socket.close()
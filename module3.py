import socket
import sys
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    my_socket.bind(("",1234))
except socket.error:
    print("FAILED TO BIND")
    sys.exit()

my_socket.listen(5)

while True:
    connection, address = my_socket.accept()
    print("GOT A REQUEST")
    data = connection.recv(1000)
    print(data)
    if not data:
        break
    connection.sendall(data)
    
connection.close()
my_socket.close()
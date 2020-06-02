import threading
import socket

bind_ip = "127.0.0.1"
bind_port = 9999
clientBuff = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5) 

print("[*]Listening on %s:%d"%(bind_ip,bind_port))

def handle_client(client_socket, clientBuffer):
    while True:
        requesj = client_socket.recv(1024)
        for i in clientBuffer:
            i.send(requesj)
    client_socket.close()

while True:
    client,addr = server.accept()
    clientBuff.append(client)
    print("[*]Accepted connection from:%s:%d"%(addr[0],addr[1]))
    client_handler = threading.Thread(target = handle_client, args = (client,clientBuff))
    client_handler.start()
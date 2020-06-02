import socket
import threading
target_host = "127.0.0.1"
target_port = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
nickName = input("请输入你的昵称：")

def sendMesage(client_socket):
    while True:
        mesage = input("[*]:")
        sendM = "(" + nickName + ")" + mesage
        client_socket.send(sendM.encode(encoding="utf-8"))

clientHandler = threading.Thread(target = sendMesage, args = (client,))
clientHandler.start()

while True:
    response = client.recv(4096)
    print(response.decode(encoding="utf-8"))
    print("[*]:")

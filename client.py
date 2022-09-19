import socket

from Expression import Expression

HEADER = 64
PORT = 5050
SERVER = "192.168.56.1"
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

while True:
    try:
        exp = Expression(input("수식을 입력하세요: "))
        send(exp.toString())
    except Exception as e:
        print(e)


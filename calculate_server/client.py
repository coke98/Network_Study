import socket
from expression import Expression

HEADER = 64
MAIN_SERVER_PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'

print("start")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, MAIN_SERVER_PORT))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client_socket.send(send_length)
    client_socket.send(message)
    print(client_socket.recv(2048).decode(FORMAT))

while True:
    try:
        exp = Expression(input("수식을 입력하세요: "))
        send(exp.to_string())
    except Exception as e:
        print(e)


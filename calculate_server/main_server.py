import socket
import threading

HEADER = 64
ADD_SUB_SERVER_PORT = 5051
MUL_DIV_SERVER_PORT = 5052
CLIENT_PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'

# TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 포트 연결
server.bind((HOST, CLIENT_PORT))

# server 포트 출력
print(server.getsockname()[1])

def handle_client(client, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            send(msg)
            client.send("Msg receivec".encode(FORMAT))
    client.close()

def start():
    server.listen()
    print(f"[LISTENiNG] Server is listening on {HOST}")
    while True:
        client, addr  = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


def send(msg):

    ADDR = (HOST, ADD_SUB_SERVER_PORT)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDR)
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client_socket.send(send_length)
    client_socket.send(message)
    print(client_socket.recv(2048).decode(FORMAT))

print("startng...")
start()
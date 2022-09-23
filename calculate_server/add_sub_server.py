import socket
import threading

HEADER = 64
MAIN_SERVER_PORT = 5051
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'

# TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 포트 연결
server.bind((HOST, MAIN_SERVER_PORT))

def handle_client(client, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            client.send("Msg receivec".encode(FORMAT))
    client.close()

def start():
    server.listen()
    print(f"[LISTENiNG] Server is listening on {HOST}")
    while True:
        client, addr  = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

print("startng...")
start()
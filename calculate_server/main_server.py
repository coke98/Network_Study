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

def handle_client(client, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            exp = client.recv(msg_length).decode(FORMAT)
            # print(f"[{addr}] {exp}")
            result_msg = send(exp)
            client.send(result_msg.encode(FORMAT))
    client.close()

def start():
    server.listen()
    print(f"[LISTENiNG] Server is listening on {HOST}")
    while True:
        client, addr  = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

# 수식을 구분하여 각 서버에 전송
def send(exp):
    # msg 가 +, - 를 포함하면 add_sub_server 로 전송
    if '+' in exp or '-' in exp:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, ADD_SUB_SERVER_PORT))
        message = exp.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client_socket.send(send_length)
        client_socket.send(message)
        return_msg = client_socket.recv(2048).decode(FORMAT)
        print(return_msg)
        return return_msg

    # msg 가 *, / 를 포함 하면 mul_div_server 로 전송
    elif '*' in exp or '/' in exp:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, MUL_DIV_SERVER_PORT))
        message = exp.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client_socket.send(send_length)
        client_socket.send(message)
        return_msg = client_socket.recv(2048).decode(FORMAT)
        print(return_msg)
        return return_msg

print("startng...")
start()
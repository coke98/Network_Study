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

# 클라이언트 핸들링 함수
def handle_client(client, addr):
    connected = True
    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            exp = client.recv(msg_length).decode(FORMAT)
            result_msg = send(exp)
            client.send(result_msg.encode(FORMAT))
    client.close()

# 서버 시작 함수
def start():
    server.listen()
    print(f"Main Server is listening")
    while True:
        client, addr  = server.accept()
        # 클라이언트가 접속하면 새로운 스레드를 생성하여 handle_client 함수를 실행
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()
        print(f"현재 쓰레드 : {threading.active_count() - 1}")

# 수식을 구분하여 각 서버에 전송
def send(exp):
    # TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # msg 가 +, - 를 포함하면 add_sub_server 로 전송
    if '+' in exp or '-' in exp:
        client_socket.connect((HOST, ADD_SUB_SERVER_PORT))
    # msg 가 *, / 를 포함 하면 mul_div_server 로 전송
    elif '*' in exp or '/' in exp:
        client_socket.connect((HOST, MUL_DIV_SERVER_PORT))
    message = exp.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client_socket.send(send_length)
    client_socket.send(message)

    # 계산 결과를 받아와 출력 및 반환
    return_msg = client_socket.recv(2048).decode(FORMAT)
    print(return_msg)
    return return_msg

start()
import socket
import threading

HEADER = 64
MAIN_SERVER_PORT = 5052
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'

# TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 포트 연결
server.bind((HOST, MAIN_SERVER_PORT))

# 클라이언트 핸들링 함수
def handle_client(client, addr):
    connected = True
    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            exp = client.recv(msg_length).decode(FORMAT)
            result = calculate(exp)
            result_msg = exp + " = " + str(result)
            print(result_msg)
            client.send(result_msg.encode(FORMAT))
    client.close()

# 서버 시작 함수
def start():
    server.listen()
    print(f"Mul,Div Server is listening")
    while True:
        client, addr  = server.accept()
        # 클라이언트가 접속하면 새로운 스레드를 생성하여 handle_client 함수를 실행
        thread = threading.Thread(target=handle_client, args=(client,addr))
        thread.start()

# 계산 함수
def calculate(exp):
    if "*" in exp:
        exp = exp.split("*")
        result = int(exp[0]) * int(exp[1])
    elif "/" in exp:
        exp = exp.split("/")
        result = int(exp[0]) / int(exp[1])
    return result

start()
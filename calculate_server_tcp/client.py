from expression import expression
import socket

HEADER = 64
MAIN_SERVER_PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'

# TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, MAIN_SERVER_PORT))
print("서버 접속 완료")

def send(exp):
    # 서버에 수식 전송
    message = exp.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client_socket.send(send_length)
    client_socket.send(message)

    # 서버로부터 결과값을 받아와 출력
    return_msg = client_socket.recv(2048).decode(FORMAT)
    print(return_msg)

while True:
    try:
        # 사용자로부터 수식 입력
        exp = expression(input("수식을 입력하세요: "))
        # 수식을 서버에 전송
        send(exp.to_string())
    except Exception as e:
        print(e)


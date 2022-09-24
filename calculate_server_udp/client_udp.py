from expression import expression
import socket

HEADER = 64
MAIN_SERVER_PORT = 6050
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'

# UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((HOST, MAIN_SERVER_PORT))
print("서버 접속 완료")

def send(exp):
    # 서버에 수식 전송
    client_socket.sendto(exp.encode(FORMAT), (HOST, MAIN_SERVER_PORT))

    # 서버로부터 결과값을 받아와 출력
    return_msg, addr = client_socket.recvfrom(200)

    print(return_msg.decode(FORMAT))

while True:
    try:
        # 사용자로부터 수식 입력
        exp = expression(input("수식을 입력하세요: "))
        # 수식을 서버에 전송
        send(exp.to_string())
    except Exception as e:
        print(e)


import socket

HEADER = 64
ADD_SUB_SERVER_PORT = 6051
MUL_DIV_SERVER_PORT = 6052
CLIENT_PORT = 6050
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'

# UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 포트 연결
server.bind((HOST, CLIENT_PORT))

# 서버 시작 함수
def start():
    print(f"Main Server is listening")
    while True:
        exp, addr = server.recvfrom(200)
        result_msg = send(exp.decode(FORMAT))
        server.sendto(result_msg, addr)    

# 수식을 구분하여 각 서버에 전송
def send(exp):
    # UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # msg 가 +, - 를 포함하면 add_sub_server 로 전송
    if '+' in exp or '-' in exp:
        client_socket.sendto(exp.encode(FORMAT), (HOST, ADD_SUB_SERVER_PORT))
        
    # msg 가 *, / 를 포함 하면 mul_div_server 로 전송
    elif '*' in exp or '/' in exp:
        client_socket.sendto(exp.encode(FORMAT), (HOST, MUL_DIV_SERVER_PORT))

    # 계산 결과를 받아와 출력 및 반환
    result_msg, addr = client_socket.recvfrom(200)
    return result_msg 

start()
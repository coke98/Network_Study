import socket

HEADER = 64
MAIN_SERVER_PORT = 6052
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'

# UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 포트 연결
server.bind((HOST, MAIN_SERVER_PORT))

# 서버 시작 함수
def start():
    print(f"Mul,Div Server is listening")
    while True:
        exp, addr = server.recvfrom(200)
        result = calculate(exp.decode(FORMAT))
        result_msg = exp.decode(FORMAT) + " = " + str(result)
        server.sendto(result_msg.encode(FORMAT), addr)   

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
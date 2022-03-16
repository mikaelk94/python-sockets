import socket

HOST = '127.1.2.3'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input('Enter message: ')
        s.send(message.encode())
        data = s.recv(1024)
        print('Server > ', data.decode())
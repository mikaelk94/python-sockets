import socket
import threading

IP = '127.1.2.3'
PORT = 65432
connection_count = 0

def new_client(conn, addr):
    while True:
        data = conn.recv(1024)
        if data:
            print(f'{addr} > ', data.decode())
            conn.send(data)
        else:
            global connection_count
            connection_count = connection_count - 1
            print(f'Disconnected by {addr}, current connections: {connection_count}')
            break
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen()
    print(f'Listening for connections on {IP}:{PORT}')
    while True:
        conn, addr = s.accept()
        connection_count+=1
        print(f'Connected by {addr}, current connections: {connection_count}')
        thread = threading.Thread(target=new_client, args=(conn, addr))
        thread.start()
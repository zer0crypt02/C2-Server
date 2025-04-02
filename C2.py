import socket
import threading

def handle_client(client_socket, address):
    print(f'New connection from {address}')

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f'Received data: {data}')
        response = 'Server received: ' + data
        client_socket.send(response.encode())

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.4', 4321))
    server_socket.listen(1)
    print('Server is listening on 192.168.1.4:4321')

    while True:
        client_socket, address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

if __name__ == '__main__':
    start_server()
    
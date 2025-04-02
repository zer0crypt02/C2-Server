import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.4', 4444))
    print('Connected to server')

    while True:
        message = input('Enter a message (or "q" to quit): ')
        if message == 'q':
            break
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f'Server response: {response}')

    client_socket.close()

if __name__ == '__main__':
    start_client()
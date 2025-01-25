import socket

def client_program():
    host = socket.gethostbyname(socket.gethostname())
    port = 65432


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("Client-> ")

    while message.lower().strip() != 'bye':
        print(f"Sending to server: {message}")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input("Client-> ")

    client_socket.close()

client_program()

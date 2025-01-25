import socket
import threading

def handle_client(conn, addr):
    connected = True
    while connected:
        data = conn.recv(1024).decode()
        if not data:
            connected = False
        else:
            print("Received from client " + str(addr) + ": " + str(data))
            data = input('Server message to send-> ')
            print(f"Sending to client: {data}")
            conn.send(data.encode())
    conn.close()
    print(f"Active connections: {threading.active_count() - 2}")

def server_program():
    host = socket.gethostbyname(socket.gethostname())
    port = 65432

    print(f"Server starting with ip-address: {host} and port: {port}")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    while True:
        print("Accepting connection from a client")
        conn, addr = server_socket.accept()
        print("Connection established with: " + str(addr))
        # Each connection will run in a separate thread
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")

server_program()

import socket
import threading

def handle_client(client_socket, client_address):
    print("Client connected:", client_address)

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        message = data.decode()
        print("Received message from", client_address, ":", message)

        if message == "ping":
            response = "pong"
            client_socket.sendall(response.encode())

    print("Client disconnected:", client_address)
    client_socket.close()

def main():
    server_ip = "localhost"
    server_port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    print("Server listening on", server_ip, ":", server_port)

    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    main()

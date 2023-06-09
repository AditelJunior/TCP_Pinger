import socket
import os
import json
import csv
import sys
import matplotlib.pyplot as plt

def send_ping(server_ip, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        message = "ping"
        client_socket.sendall(message.encode())

        data = client_socket.recv(1024)
        response = data.decode()
        print("Server response:", response)

        client_socket.close()
    except Exception as e:
        print("Error occurred:", str(e))

def send_file(server_ip, server_port, file_path):
    try:
        if not os.path.exists(file_path):
            print("File does not exist.")
            return

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))

        file_name = os.path.basename(file_path)
        client_socket.sendall(file_name.encode())

        with open(file_path, "rb") as file:
            data = file.read(1024)
            while data:
                client_socket.sendall(data)
                data = file.read(1024)

        client_socket.close()
        print("File sent successfully.")
    except Exception as e:
        print("Error occurred:", str(e))

def receive_file(server_ip, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))

        file_name = client_socket.recv(1024).decode()
        if not file_name:
            print("No file name received.")
            return

        with open(file_name, "wb") as file:
            data = client_socket.recv(1024)
            while data:
                file.write(data)
                data = client_socket.recv(1024)

        client_socket.close()
        print("File received successfully:", file_name)
    except Exception as e:
        print("Error occurred:", str(e))

def visualize_image(file_path):
    try:
        img = plt.imread(file_path)
        plt.imshow(img)
        plt.axis("off")
        plt.show()
    except Exception as e:
        print("Error occurred while visualizing image:", str(e))

def visualize_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print(data)
    except Exception as e:
        print("Error occurred while visualizing CSV:", str(e))

def visualize_json(file_path):
    try:
        with open(file_path) as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))
    except Exception as e:
        print("Error occurred while visualizing JSON:", str(e))

def broadcast_file(server_ip, server_port, file_path):
    try:
        if not os.path.exists(file_path):
            print("File does not exist.")
            return

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))

        file_name = os.path.basename(file_path)
        client_socket.sendall(file_name.encode())

        with open(file_path, "rb") as file:
            data = file.read(1024)
            while data:
                client_socket.sendall(data)
                data = file.read(1024)

        client_socket.close()
        print("File broadcasted successfully.")
    except Exception as e:
        print("Error occurred:", str(e))

def menu():
    print("Menu:")
    print("1. Send Ping")
    print("2. Send File")
    print("3. Receive File")
    print("4. Visualize Image")
    print("5. Visualize CSV")
    print("6. Visualize JSON")
    print("7. Broadcast File")
    print("8. Exit")

def main():
    server_ip = "localhost"
    server_port = 8888

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            send_ping(server_ip, server_port)
        elif choice == "2":
            file_path = input("Enter the file path to send: ")
            send_file(server_ip, server_port, file_path)
        elif choice == "3":
            receive_file(server_ip, server_port)
        elif choice == "4":
            file_path = input("Enter the image file path: ")
            visualize_image(file_path)
        elif choice == "5":
            file_path = input("Enter the CSV file path: ")
            visualize_csv(file_path)
        elif choice == "6":
            file_path = input("Enter the JSON file path: ")
            visualize_json(file_path)
        elif choice == "7":
            file_path = input("Enter the file path to broadcast: ")
            broadcast_file(server_ip, server_port, file_path)
        elif choice == "8":
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

import socket
import os

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_ip = input("Enter the server IP: ")
port = 12345
client_socket.connect((server_ip, port))

# Ask the user if they want to upload or download a file
command = input("Do you want to upload or download a file? (upload/download): ")
client_socket.send(command.encode())

if command == "upload":
    # Get the file name
    filename = input("Enter the file name: ")
    client_socket.send(filename.encode())

    # Get the file size
    file_size = os.path.getsize(filename)
    client_socket.send(str(file_size).encode())
    client_socket.recv(1024)

    # Send the file
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(1024), b""):
            client_socket.send(chunk)

    print(f"{filename} uploaded successfully")

elif command == "download":
    # Get the list of files from the server
    files = client_socket.recv(1024).decode().split(";")
    print("Files available for download:", files)

    # Get the file name
    filename = input("Enter the file name: ")
    client_socket.send(filename.encode())

    # Get the file size
    file_size = int(client_socket.recv(1024).decode())
    client_socket.send(b"ACK")

    # Receive the file
    with open(filename, "wb") as f:
        received_size = 0
        while received_size < file_size:
            chunk = client_socket.recv(1024)
            received_size += len(chunk)
            f.write(chunk)

    print(f"{filename} downloaded successfully")

else:
    print("Invalid command")

# Close the connection
client_socket.close()

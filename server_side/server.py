import socket
import os

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('0.0.0.0', 12345)
server_socket.bind(server_address)

# Start listening for incoming connections
server_socket.listen(1)
print(f"Server listening on {server_address[0]}:{server_address[1]}")

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Client connected from {client_address[0]}:{client_address[1]}")

    # Receive the command from the client
    command = client_socket.recv(1024).decode()
    if command == "upload":
        # Receive the file name
        filename = client_socket.recv(1024).decode()
        print(f"Receiving file {filename}...")

        # Receive the file size
        file_size = int(client_socket.recv(1024).decode())
        client_socket.send(b"ACK")

        # Receive the file
        with open(f"files/{filename}", "wb") as f:
            received_size = 0
            while received_size < file_size:
                chunk = client_socket.recv(1024)
                received_size += len(chunk)
                f.write(chunk)

        print(f"{filename} received successfully")

    elif command == "download":
        # Send the list of files
        files = os.listdir("files")
        client_socket.send(";".join(files).encode())

        # Receive the file name
        filename = client_socket.recv(1024).decode()
        print(f"Sending file {filename}...")

        # Send the file size
        file_size = os.path.getsize(f"files/{filename}")
        client_socket.send(str(file_size).encode())
        client_socket.recv(1024)

        # Send the file
        with open(f"files/{filename}", "rb") as f:
            for chunk in iter(lambda: f.read(1024), b""):
                client_socket.send(chunk)

        print(f"{filename} sent successfully")

    else:
        print("Invalid command")

    # Close the connection
    client_socket.close()
    print(f"Client disconnected from {client_address[0]}:{client_address[1]}")

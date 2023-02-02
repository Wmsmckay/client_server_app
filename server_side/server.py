import socket
import sys
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 10000)
print(f'starting up on {server_address[0]} port {server_address[1]}')
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print(f'connection from {client_address}')

    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(16).decode()
        print(f'received {data}')
        if data == 'UPLOAD':
            connection.sendall('ACK'.encode())
            filename = connection.recv(1024).decode()
            with open(f'files/{filename}', 'wb') as f:
                while True:
                    file_data = connection.recv(1024)
                    if not file_data:
                        break
                    f.write(file_data)
            connection.sendall('ACK'.encode())
        elif data == 'DOWNLOAD':
            if os.listdir('files'):
                connection.sendall('ACK'.encode())
                files = os.listdir('files')
                connection.sendall(str(files).encode())
                filename = connection.recv(1024).decode()
                with open(f'files/{filename}', 'rb') as f:
                    while True:
                        file_data = f.read(1024)
                        if not file_data:
                            break
                        connection.sendall(file_data)
                connection.sendall('ACK'.encode())
            else:
                connection.sendall('EMPTY'.encode())
        elif data:
            response = f'ACK: {data}'
            connection.sendall(response.encode())
        else:
            print(f'no more data from {client_address}')
            break

    # Clean up the connection
    connection.close()

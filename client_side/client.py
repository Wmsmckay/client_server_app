import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 10000)
print(f'connecting to {server_address}')
sock.connect(server_address)

try:
    while True:
        # Read user input
        message = input("Enter a command (UPLOAD/DOWNLOAD/QUIT): ")

        # Send the user input to the server
        sock.sendall(message.encode('utf-8'))

        # Check if the user wants to upload a file
        if message.startswith('UPLOAD'):
            filename = message.split()[1]
            with open(filename, 'rb') as f:
                data = f.read()
                sock.sendall(data)
            print(f'{filename} has been sent to the server.')
        elif message.startswith('DOWNLOAD'):
            filename = message.split()[1]
            sock.sendall(filename.encode('utf-8'))
            data = sock.recv(1024)
            if data == b'FILE NOT FOUND':
                print(f'{filename} not found on the server.')
            else:
                with open(filename, 'wb') as f:
                    f.write(data)
                print(f'{filename} has been downloaded from the server.')
        elif message == 'QUIT':
            print('Closing the connection.')
            break
        else:
            # Receive the response from the server
            data = sock.recv(1024)
            print(f'received {data.decode("utf-8")}')

finally:
    # Clean up the socket
    print('Closing socket')
    sock.close()
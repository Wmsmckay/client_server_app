# Overview

This project is a client-server application in Python that allows users to upload and download files between the client and server. The application is capable of handling multiple connections, making it a multi-user file sharing system.

To start the client, run the client.py file. The client will prompt the user to enter the IP address of the server. Then, the user can choose to either upload or download a file. If the user chooses to upload a file, the client will ask for the file name and send the file size and file data to the server. If the user chooses to download a file, the client will receive a list of available files from the server, then ask for the desired file name and receive the file data from the server.

To start the server, run the server.py file. The server will listen for incoming connections on port 12345. When a client connects, the server will receive the command from the client and take action accordingly. If the command is to upload a file, the server will receive the file name, file size, and file data from the client. If the command is to download a file, the server will send the list of available files, file size, and file data to the client.

(The client and server need to be ran on separate devices)

[Software Demo Video](https://youtu.be/-jeNZ9PYGSg)

# Network Communication

The network communication in this project uses TCP, which is a reliable protocol that ensures that all data is transmitted correctly. The client and server are connected on port 12345, which was picked arbitrarily because it was available on both the client and server being used. The messages exchanged between the client and server are encoded and decoded using the encode and decode methods. This ensures that the messages are sent and received correctly between the client and server.

# Development Environment

* VS Code
* Git/Github
* Python 3.8 64-bit
* Ubuntu 20.04 LTS (virtual machine running server software)
* Python socket library

# Useful Websites

* [Python Socket Server](https://docs.python.org/3.6/library/socketserver.html)
* [File Transfer using TCP Socket in Python3](https://idiotdeveloper.com/file-transfer-using-tcp-socket-in-python3/)

# Future Work

* Containerize server side code for easy deployment
* Improve the user interface to make uploading and downloading more friendly
* Expand server to handle not overwriting files and transferring multiple files at once
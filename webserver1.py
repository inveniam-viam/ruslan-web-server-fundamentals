import socket


# HOST being set to an empty string means that the server will be listening on all available interfaces
# that is, it is not restricted to a single IP address of your machine but can accept connections from any network interface (localhost, LAN etc.)
HOST, PORT = '', 8888
# PORT being set to 8888 - this is the port number on which your server will be listening for incoming connections
# resemble address numbers in networking

# creating a socket

# when creating a socket, we need to specify the address family (which is what is accomplished using AF_INET)
# AF_INET is an address family that is used to designate the type of addresses the socket CAN COMMUNICATE WITH
# once we've specified AF_INET, we can only use addresses of that type with the socket
listen_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SOCK_STREAM specifies the socket type - SOCK_STREAM implies the socket will use TCP

listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# method call on the listen_socket soecket object 
# setsockopt sets the options for the socket, allowing for reconfiguration of its behavior
# SOL_SOCKET means that the option is one that applies to sockets as opposed to protocol
# socket.SO_REUSEADDR tells the kernel to allow for the reuse of local addresses in bind calls
# 1 means True, which means SO_REUSEADDR is being enabled

listen_socket.bind((HOST, PORT))
# binding the socket we created using the listen_socket variable to the HOST and PORT we initialized before
# bind takes a tuple - when a socket is bound to a host and port, it means it is tied to a specific network interface and port number on your machine
# necessary so the server knows where to listen for incoming connections

listen_socket.listen(1)
# after the binding, we typically put the socket into a listening state where it can accept connections

print(f"Serving HTTP on port {PORT}...")

while True:

    client_connection: socket.socket 
    client_address: tuple
    client_connection, client_address = listen_socket.accept()
    # when a client connects to the server, the listen_socket socket object accepts the connection
    # it then returns a new socket object representing the connection made
    # and a tuple client_address containing the client's address

    request_data = client_connection.recv(1024)
    # reads the request sent by the client to the server (reads UP TO 1024 bytes from the connection)
    print(request_data.decode('utf-8'))
    # decodes the request data from bytes to a string using UTF-8 and prints it
    http_response = b"""\
HTTP/1.2 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    # sends the HTTP response back to the client

    client_connection.close()
    # closes the connection to the client. after sending the response, the server no longer needs to keep the connection open
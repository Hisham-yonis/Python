import socket

Host = 'localhost'
Port = 65432    

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((Host, Port))
    print(f"Connected to server at {Host}:{Port}")
    
    message = "Hello, Server!"
    client_socket.sendall(message.encode())
    print(f"Sent: {message}")
    
    response = client_socket.recv(1024)
    print(f"Received: {response.decode()}")
    client_socket.close()
    print("Connection closed.")
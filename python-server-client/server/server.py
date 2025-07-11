import socket

Host = 'localhost'
Port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((Host, Port))
    server_socket.listen()
    print(f"Server listening on {Host}:{Port}")
    conn, addr = server_socket.accept()

    with conn:
        print("Client connected.")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            response = "Hello, Client!"
            conn.sendall(response.encode())
            print(f"Sent: {response}")
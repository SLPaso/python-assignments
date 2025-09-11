import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening...")

    try:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")
        conn.sendall(b"Hello from server!")
        conn.close()
    except Exception as e:
        print("An error occurred:", e)
    finally:
        server_socket.close()

start_server()
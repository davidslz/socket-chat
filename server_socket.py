import socket

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Utiliza la direccion IP de la PC para vincular el socket con una direccion
        #server_address = (socket.gethostbyname(socket.gethostname()), 65432)
        # Utiliza la interfaz loop de la PC
        server_address = ("127.0.0.1", 65432)

        server.bind(server_address)

        server.listen(0)
        print(f"Servidor escuchando {server_address[0]}:{server_address[1]}")

        client_socket, client_address = server.accept()

        with client_socket:
            print(f"Conexion aceptada con {client_address[0]}:{client_address[1]}")
            while True:            
                request = client_socket.recv(1024)
                request = request.decode("utf-8")

                if request.lower() == "end":
                    client_socket.send("closed".encode("utf-8"))
                    break

                print(f"mensaje: {request}")

                response = "recibido".encode("utf-8")
                client_socket.send(response)
    
    print("conexion terminada")


run_server()

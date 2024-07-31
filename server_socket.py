import socket
import threading

def client_conecction(client_socket, client_address):
    user = client_socket.recv(1024)
    user = user.decode("utf-8")
    print(f"Conexion aceptada con usuario {user} <{client_address[0]}:{client_address[1]}>")
    while True:            
        request = client_socket.recv(1024)
        request = request.decode("utf-8")
            
        if request.lower() == "end":
            client_socket.send("closed".encode("utf-8"))
            break

        print(f"{user}: {request}")

        response = "recibido".encode("utf-8")
        client_socket.send(response)

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Utiliza la direccion IP de la PC para vincular el socket con una direccion
        #server_address = (socket.gethostbyname(socket.gethostname()), 65432)
        # Utiliza la interfaz loop de la PC
        server_address = ("127.0.0.1", 65432)

        server.bind(server_address)

        server.listen(0)
        print(f"Servidor escuchando {server_address[0]}:{server_address[1]}")

        while True: 
            client_socket, client_address = server.accept() 

            thread = threading.Thread(target=client_conecction, args=(client_socket,client_address))
            thread.start()

    print("conexion terminada")


run_server()

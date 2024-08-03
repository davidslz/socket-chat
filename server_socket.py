import socket
import threading

clientes = 0


def client_conecction(client_socket, client_address):
    nickname = client_socket.recv(1024)
    nickname = nickname.decode("utf-8")
    #print(f"Conexion aceptada con usuario {nickname} <{client_address[0]}:{client_address[1]}>")
    global clientes
    clientes += 1
    users = {}

    usuario = "user" + str(clientes)

    users[usuario]= {'name' : nickname,'address' : client_address[0],'port' : client_address[1]}

    print("nueva conexion con:  ",users[usuario]['name'],users[usuario]['address'],users[usuario]['port'])

    while True:            
        request = client_socket.recv(1024)
        request = request.decode("utf-8")
            
        if request.lower() == "end":
            client_socket.send("closed".encode("utf-8"))
            break

        print(f"{nickname}: {request}")

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

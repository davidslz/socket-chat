import socket

def run_client():
    nickname = input("Elige un alias: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        server_address = ("127.0.0.1",65432)

        cliente.connect(server_address)
        cliente.send(nickname.encode("utf-8"))
        while True:
            mensaje = input("Ingresa el mensaje: ").encode("utf-8")
            cliente.send(mensaje)

            server_response = cliente.recv(1024)
            server_response = server_response.decode("utf-8")
            print(server_response)

            if server_response.lower() == "closed":
                break

    print("socket cerrado")


run_client()    
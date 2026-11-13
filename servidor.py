"""
Servidor TCP mínimo con sockets.

Objetivo de la práctica (PFO1 de Programación sobre Redes): establecer
conexiones entre procesos, enviar y recibir mensajes, y manejar los
errores comunes (cliente que se desconecta de golpe, mensajes vacíos).

Atiende un cliente a la vez, uno detrás del otro, a propósito: alcanza
para demostrar el protocolo cliente-servidor sin meter threads todavía
(eso es la PFO3, que sí pide concurrencia).
"""
import socket

HOST = "0.0.0.0"
PUERTO = 9000


def atender_cliente(conexion, direccion):
    print(f"[servidor] Cliente conectado desde {direccion}")
    try:
        while True:
            datos = conexion.recv(1024)
            if not datos:
                # El cliente cerró la conexión de su lado.
                print(f"[servidor] {direccion} se desconectó")
                break

            mensaje = datos.decode("utf-8").strip()
            print(f"[servidor] Recibido de {direccion}: {mensaje!r}")

            if mensaje.lower() == "salir":
                conexion.sendall(b"Chau!\n")
                break

            respuesta = f"Servidor recibio: {mensaje}\n"
            conexion.sendall(respuesta.encode("utf-8"))
    except ConnectionResetError:
        # El cliente se cayó sin avisar (ej: cerró la terminal de golpe).
        print(f"[servidor] {direccion} cortó la conexión de forma abrupta")
    finally:
        conexion.close()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PUERTO))
        servidor.listen()
        print(f"[servidor] Escuchando en {HOST}:{PUERTO} (Ctrl+C para salir)")

        while True:
            conexion, direccion = servidor.accept()
            atender_cliente(conexion, direccion)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[servidor] Apagado por el usuario")

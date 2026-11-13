"""
Cliente TCP mínimo con sockets.

Se conecta al servidor, manda líneas que escribe el usuario por consola,
y muestra la respuesta. Escribir "salir" corta la conexión prolijamente.
"""
import socket
import sys

HOST = "127.0.0.1"
PUERTO = 9000


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((HOST, PUERTO))
            print(f"[cliente] Conectado a {HOST}:{PUERTO}. Escribí 'salir' para cortar.")

            while True:
                mensaje = input("> ")
                if not mensaje:
                    continue

                cliente.sendall(mensaje.encode("utf-8"))

                if mensaje.lower() == "salir":
                    respuesta = cliente.recv(1024)
                    print(respuesta.decode("utf-8").strip())
                    break

                respuesta = cliente.recv(1024)
                if not respuesta:
                    print("[cliente] El servidor cerró la conexión")
                    break
                print(respuesta.decode("utf-8").strip())

    except ConnectionRefusedError:
        print("[cliente] No se pudo conectar: ¿está el servidor corriendo?")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[cliente] Cortado por el usuario")


if __name__ == "__main__":
    main()

# Cliente y servidor TCP con sockets

> ⚠️ Punto de partida para practicar sockets (PFO1 de Programación sobre
> Redes), no una entrega. Para el trabajo real, adaptalo al enunciado que
> te den.

Servidor y cliente mínimos en Python puro (sin dependencias) que
demuestran: conexión cliente-servidor, envío y recepción de mensajes, y
manejo de los dos errores más comunes — el cliente que corta la conexión
de golpe, y el cliente que intenta conectarse sin que haya servidor.

## Cómo correrlo

En una terminal:

```bash
python servidor.py
```

En otra terminal:

```bash
python cliente.py
```

Escribí lo que quieras mandar; el servidor lo devuelve con un prefijo.
Escribí `salir` para cortar la conexión de forma prolija.

## Qué maneja

- **Cliente que se desconecta de golpe** (cierra la terminal, se corta la
  red): el servidor lo detecta (`ConnectionResetError` o un `recv()` vacío)
  y sigue esperando al próximo cliente sin caerse.
- **No hay servidor corriendo**: el cliente detecta `ConnectionRefusedError`
  y avisa, en vez de colgarse.
- Atiende un cliente por vez, a propósito: así se ve el protocolo
  cliente-servidor sin la complejidad de threads (eso es tema de otra
  práctica, cuando toque atender varios clientes a la vez).

## Estructura

- `servidor.py` — escucha en el puerto `9000` y responde a cada mensaje.
- `cliente.py` — se conecta, manda lo que el usuario escribe, muestra la
  respuesta.

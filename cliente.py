import socket

def enviar_orden():
    # Tarea 2: Sockets TCP/IP
    # Usamos 127.0.0.1 para probar localmente en tu laboratorio
    ip = "127.0.0.1" 
    puerto = 6500

    while True:
        print("\n--- PANEL DE CONTROL REMOTO ---")
        print("Escribe: 'listar', 'monitorear', 'detener [PID]' o 'salir'")
        cmd = input("Orden: ")
        
        if cmd == "salir": break

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((ip, puerto))
            sock.send(cmd.encode('utf-8'))
            print(f"\nRespuesta:\n{sock.recv(4096).decode('utf-8')}")
        except:
            print("Error: No se pudo conectar al servidor.")
        finally:
            sock.close()

if __name__ == "__main__":
    enviar_orden()

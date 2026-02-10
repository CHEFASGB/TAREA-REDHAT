import socket

# TAREA 3: MIDDLEWARE Y DESCUBRIMIENTO
# En los labs de Red Hat, los nombres de dominio suelen estar preconfigurados
nodos_distribuidos = {
    "1": ("servera", 5000),
    "2": ("serverb", 5000)
}

def conectar_nodo(host, puerto, orden):
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.settimeout(3) # Si el servidor no responde en 3 seg, error
        c.connect((host, puerto))
        c.send(orden.encode())
        respuesta = c.recv(4096).decode()
        c.close()
        return respuesta
    except Exception as e:
        return f"ERROR: No se pudo conectar a {host}. ¿Está encendido el script?"

def menu():
    while True:
        print("\n--- SISTEMA DE GESTIÓN DISTRIBUIDA (RHEL) ---")
        print("Nodos disponibles:")
        for k, v in nodos_distribuidos.items():
            print(f" [{k}] {v[0]}")
        print(" [Q] Salir")

        seleccion = input("\nSeleccione un NODO: ")
        if seleccion.lower() == 'q': break
        
        if seleccion in nodos_distribuidos:
            host_destino = nodos_distribuidos[seleccion][0]
            print(f"\nConectado a {host_destino}. Comandos: listar, monitorear, detener <PID>")
            comando = input("Comando >> ")
            
            print(f"\n--- Respuesta de {host_destino} ---")
            print(conectar_nodo(host_destino, 5000, comando))
        else:
            print("Selección inválida.")

if __name__ == "__main__":
    menu()

import socket
import psutil
import os

def manejar_comando(comando):
    # Tarea 1: Listar, Detener y Monitorear
    try:
        if comando == "listar":
            # Lista los primeros 5 procesos con su PID y Nombre
            p_lista = [f"PID: {p.info['pid']} | {p.info['name']}" for p in psutil.process_iter(['pid', 'name'])]
            return "\n".join(p_lista[:5])
        
        elif comando == "monitorear":
            # Monitoreo de CPU y Memoria RAM
            cpu = psutil.cpu_percent(interval=1)
            memoria = psutil.virtual_memory().percent
            return f"Estado del Servidor: CPU al {cpu}% y RAM al {memoria}%"
        
        elif comando.startswith("detener"):
            # Detener un proceso por su número de PID
            pid = int(comando.split()[1])
            os.kill(pid, 9)
            return f"Éxito: Proceso {pid} detenido."
        
        return "Comando inválido."
    except Exception as e:
        return f"Error: {str(e)}"

# Tarea 2: Comunicación TCP/IP por Sockets
def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("0.0.0.0", 6500)) # Escucha en el puerto 6500
    servidor.listen(1)
    print("Servidor activo en RHEL. Esperando conexión del cliente...")

    while True:
        cliente, _ = servidor.accept()
        pedido = cliente.recv(1024).decode('utf-8')
        respuesta = manejar_comando(pedido)
        cliente.send(respuesta.encode('utf-8'))
        cliente.close()

if __name__ == "__main__":
    iniciar_servidor()

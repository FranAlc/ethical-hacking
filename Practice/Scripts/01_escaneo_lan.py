#Escaneo de red LAN
#/24 -> 255.255.255.0
#/16 -> 255.255.0.0
#/8 -> 255.0.0.0
import subprocess

def nmap(ip):
    print(f"IP: {ip}")
    sh = f"nmap -sn {ip}/24"
    try:
        outp = subprocess.check_output(sh, shell=True)
        outp_str = outp.splitlines()
        for linea in outp_str:
            print(linea)
    except Exception as e:
        return f"Error en el escaneo de redes. {e}"            

ip = input("Digite su IP: ")
nmap(ip)
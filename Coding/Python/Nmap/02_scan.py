#Script para ingresar una IP para escanear y buscar puertos abiertos en ella.
import subprocess

def scan_nmap_attack(ip):
        print("Digite el timing de escaneo.")
        t =int(input("-T: "))
        if t > -1 and t < 6:
                console = f"sudo nmap -sS -p- {ip} -T{t}"
                try:
                        output = subprocess.check_output([console], shell=True)
                        output_str = output.decode("utf-8")
                        print(output_str)
                except Exception as e:
                        return "Error para realizar el escaneo."
        else: return "No se permite un timing mayor a 5."
def scan_nmap_attack_sV(ip):
        print("")
        list_puertos = []
        print("Ahora se mostrara el SO de la IP ingresada y se especificara el escaneo de puertos.")
        print("Digite el timing de escaneo nuevamente.")
        t = int(input("-T: "))
        if t > -1 and t < 6:
                cant_puertos = int(input("Digite la cantidad de puertos a escanear: "))
                for i in range(1,cant_puertos+1):
                        puertos= input(f"{i}.Puerto: ")
                        list_puertos.append(puertos)
                        valores_lista_puertos = ','.join(list_puertos)
                console = f"sudo nmap -sV -p {valores_lista_puertos} {ip} -T{t}"
                try:
                        output = subprocess.check_output([console] , shell=True)
                        output_str = output.decode("utf-8")
                        print(output_str)
                except Exception as e:
                        return "Error para realizar el segundo escaneo."
        else: return "No se permite un timing mayor a 5."

print("Digite la IP a escanear.")
ip = input("IP: ")
#Escaneo 1
scan_nmap_attack(ip)
#Escaneo 2
scan_nmap_attack_sV(ip)
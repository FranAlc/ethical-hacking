#Script para saber tu ip y encontrar redes locales.
import subprocess

def search_ip():
        print("Mostrar tu IP: ")
        ip_busqueda_sh = f"ip a | grep 'eth0'"
        try:
                output_my_ip = subprocess.check_output([ip_busqueda_sh], shell= True)
                output_str = output_my_ip.decode("utf-8")
                return print(output_str.strip()) #eliminamos espacios
                #forma 2
                """
                eth0_view = None #cancelamos que se muestre
                for view_line in output_str.splitlines():
                        if "eth0" in view_line:
                                eth0_view = view_line #logramos que se muestre
                                break

                if eth0_view: return etho_view
                else: print("La interfaz eth0 no fue encontrada")
                """
        except Exception  as e:
                return print("Error. No se pudo encontrar tu IP.")

def scan_nmap_redes(ip):
        print(f"IP ingresada: {ip}")
        print("Escaneo de redes locales:")
        print("")

        redes_ip = f"nmap -sn {ip}/24"
        try:
                output_redes_ip = subprocess.check_output(redes_ip,shell=True)
                output_redes_ip_str = output_redes_ip.decode('utf-8')
                print(output_redes_ip_str)
        except Exception as e:
                print("Error para la escaneo de Redes.")


search_ip()

my_ip = input("Digite su IP -> ")
print("")
scan_nmap_redes(my_ip)
print("Escriba el comando ping junto a la IP a atacar y cancele con [ctrl+c].")
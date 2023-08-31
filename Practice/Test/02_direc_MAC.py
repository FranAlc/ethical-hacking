#Programa que cambia la direccion MAC
import subprocess
import optparse

#1
interface = "eth0"
new_mac = "00:11:22:33:44:77"

print("[+] Se ha cambiado la direccion MAC.." + interface + " to " + new_mac)

subprocess.call(f"ifconfig {interface}  down",shell=True)
subprocess.call(f"ifconfig {interface}  hw ether  {new_mac}",shell=True)
subprocess.call(f"ifconfig {interface}  up",shell=True)

#2
interface = input("interface > ")
new_mac = input("mac > ")

print(f"[+] Se cambio con exito la direccion MAC de la interfaz {interface} a {new_mac}")

subprocess.call(f"ifconfig {interface} down", shell= True)
subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)

#3
#Este programa que realice esta mejor estructurado
def obtener_argumentos():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest= "interface", help= "Interface para cambiar direccion MAC")
    parser.add_option("-m","--mac", dest= "new_mac", help= "Nueva direccion MAC")
    return parser.parse_args()


def cambiar_mac(interface,new_mac):
    print(f"[+] Se cambio con exito la direccion MAC de la interfaz {interface} a {new_mac}")

    subprocess.call(["ifconfig", interface , "down"])
    subprocess.call(["ifconfig", interface , "hw", "ether" , new_mac])
    subprocess.call(["ifconfig", interface , "up"])


#variables globales

(options,arguments) = obtener_argumentos()
cambiar_mac(options.interface,options.new_mac)
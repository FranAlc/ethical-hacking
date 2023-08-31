#Programa que cambia la direccion MAC
import subprocess

#1
interface = "eth0"
new_mac = "00:11:22:33:44:77"

print("[+] Se ha cambiado la direccion MAC.." + interface + " to " + new_mac)

subprocess.call(f"ifconfig {interface}  down",shell=True)
subprocess.call(f"ifconfig {interface}  hw ether  {new_mac}",shell=True)
subprocess.call(f"ifconfig {interface}  up",shell=True)


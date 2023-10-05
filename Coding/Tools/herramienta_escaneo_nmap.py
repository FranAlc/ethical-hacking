#Herramienta nmap
import subprocess
import time
#Escaneos
def escaneo_rapido_ruidoso(ip):
    consola_command = f"nmap -sS -p- --open --min-rate 5000 -v -n {ip} > escaneo_rapido.txt"
    subprocess.call([consola_command],shell=True)

def escaneo_normal(ip):
    consola_command = f"nmap -p- --open {ip} > escaneo_normal.txt"
    subprocess.call([consola_command],shell=True)
    
def escaneo_silencioso(ip):
    consola_command = f"nmap -sS -p- -T2 -n {ip} > escaneo_silencioso.txt"
    subprocess.call([consola_command],shell=True)

def escaneo_servicios(ip):
    consola_command = f"nmap -sS -sC -O -T2 {ip} > escaneo_servicios.txt "    
    subprocess.call([consola_command],shell=True)

#Base del programa o Main
def elegir_escaneo():
    while True:
        try: 
            print("1. Escaneo rapido pero ruidoso.")    
            print("2. Escaneo de puertos normal.")
            print("3. Escaneo silencioso.")
            print("4. Escanear servicios y versiones.")
            print("5. Salir")
            opcion = int(input("Digite una opcion -> "))
            if opcion == 1:
                print("\n1. Escaneo rapido pero ruidoso.")    
                print("Escaneando..")
                time.sleep(3) 
                escaneo_rapido_ruidoso(ip)
                print("Guardado en un archivo llamado escaneo_normal.txt")
                print("Ejecute el comando ls y cat [archivo] .")
                break
            if opcion == 2:
                print("\n2. Escaneo de puertos normal.")
                print("Escaneando..")
                time.sleep(3)
                escaneo_normal(ip)
                print("Guardado en un archivo llamado escaneo_normal.txt")
                print("Ejecute el comando ls y cat [archivo] .")
                break
            if opcion == 3:
                print("\n3. Escaneo silencioso")   
                print("Escaneando..")
                time.sleep(3)
                escaneo_silencioso(ip)
                print("Guardado en un archivo llamado escaneo_silencioso.txt")
                break
            if opcion == 4:
                print("\n4. Escanear servicios y versiones.")   
                print("Escaneando..")
                time.sleep(3) 
                escaneo_servicios(ip)
                print("Guardado en un archivo llamado escaneo_servicios.txt ")
                break
            if opcion == 5:
                print("\nSalio con exito.")
                break
            if opcion < 1 or opcion > 5:
                print("\nIngrese un valor valido.")
                
        except KeyboardInterrupt as e:
            print(f"\nPrograma interrumpido..{e}")
    print("Fin del programa..")    


        
        

print("Programa para escanear puertos en una red:")
ip = input("\nDigite la ip -> ")
elegir_escaneo()
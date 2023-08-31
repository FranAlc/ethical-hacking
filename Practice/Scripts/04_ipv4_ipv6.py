import subprocess
import time

search_ipv4 = f"ifconfig 'eth0' | grep -oP 'inet \K[\d.]+ '"
search_ipv6 = f"ifconfig 'eth0' | grep -oP 'inet6 \K[0-9a-fA-F:]+'"

def get_ipv4_ipv6():
    print("Ejecutando codigo..")
    print("Ejecutando tu direccion IPv4 y IPv6..")
    time.sleep(2)
    try:
        outp_ipv4 = subprocess.check_output([search_ipv4], shell=True)
        outp_ipv6 = subprocess.check_output([search_ipv6], shell=True)
        outp_str4 = outp_ipv4.decode("utf-8")
        outp_str6 = outp_ipv6.decode("utf-8")
        print(f"\nTu direccion IPv4 es: {outp_str4}Tu direccion IPv6 es: {outp_str6}")
        
    except Exception as e:
        time.sleep(3)
        print(f"Error en la busqueda ip \n {e}")



if __name__ == "__main__":
    try:
        print("Codigo de ver IPs..")
        get_ipv4_ipv6()
    except (KeyboardInterrupt):
        print("\nEl programa fue interrumpido..")
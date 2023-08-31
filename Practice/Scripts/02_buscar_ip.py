#Buscar tu IP con un comando python
import subprocess

def search_ip():
    command_search_ip = f"ip a | grep 'eth0'"

    try: 
            output = subprocess.check_output([command_search_ip], shell= True)
            output_str = output.decode("utf-8")
            return print(output_str.strip()) #eliminamos espacios
    except Exception as e:
        return "Error en la busqueda de IP."    
    
search_ip()  
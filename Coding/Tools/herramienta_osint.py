import argparse
import requests

def argparse_funcion():
    parse = argparse.ArgumentParser() #llama al objeto ArgumentParser

    #agrego los argumentos que utilizara el script

    parse.add_argument('-u','--url',required= True,default='',help="Ingreso de url.")
    parse.add_argument('-f','--file',required= False,default='',help="Aloja la salida en un archivo txt.")
    #parse.add_argument('-rs','--red_social',required= False,default='',help="Devuelve redes sociales.")
    


    argumentos = parse.parse_args()#analiza los argumentos que fueron especificados

    if argumentos.url:
        url = argumentos.url #argumentos toma el valor del argumento que se mencione (url)
        if argumentos.file:
            try:
                respuesta = requests.get(url)  #respuesta toma el valor de la petición url

                respuesta.raise_for_status() #verifica si la solicitud dada anteriormente fue exitosa
                print("Solicitud Exitosa.")#http 200

                with open(argumentos.file, 'w') as archivo: #'w' abrir un archivo en modo escritura, si existe el archivo lo reemplaza
                    try:
                        archivo.write(respuesta.text)
                        print(f"Contenido HTML guardado en {argumentos.file}")
                    except:
                        print("Error al intentar ejecutar el archivo.")

            except requests.exceptions.HTTPError as e_http:
                print(f"Error, {e_http}")#devuelve Errores http (404,500)
            except requests.exceptions.RequestException as r_e:
                print(f"Error, {r_e}")#devuelve Errores de red o comunicaciones
    else:
        print("No se proporciono una url.")


    """
    [request].status_code -> Verifica si la solicitud HTTP fue exitosa o si ocurrió algún problema.
    Solicitud exitosa = 200
    No se encontro en el servidor la petición = 404
    Error interno dentro del servidor = 500
    """
        

if __name__ == "_main_":
    argparse_funcion()
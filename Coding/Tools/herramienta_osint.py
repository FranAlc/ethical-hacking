import argparse
import requests

def argparse_funcion(url):
    parse = argparse.ArgumentParser('Ejemplo >>script.py -u [url]') #llama al objeto ArgumentParser

    #agrego los argumentos que utilizara el script
    parse.add_argument('-f','--file',required= False,default='',help="Aloja la salida en un archivo txt.")
    parse.add_argument('-rs','--red_social',required= False,default='',help="Devuelve redes sociales.")
    parse.add_argument('-u','--url',required= True,default='',choices=['url'],help="Ingreso de url.")


    argumentos = parse.parse_args()#analiza los argumentos que fueron especificados

    if argumentos.url == True:
        url = argumentos.url #argumentos toma el valor del argumento que se mencione (url)
        if argumentos.file == True:
            try:
                respuesta = requests.get(url)  #respuesta toma el valor de la petición url

                respuesta.raise_for_status() #verifica si la solicitud dada anteriormente fue exitosa
                print("Solicitud Exitosa.")#http 200

                """
                print()
                    guardar la información en un txt

                """

            except requests.exceptions.HTTPError as e_http:
                print(f"Error, {e_http}")#devuelve Errores http (404,500)
            except requests.exceptions.RequestException as r_e:
                print(f"Error, {r_e}")#devuelve Errores de red o comunicaciones

    """
    [request].status_code -> Verifica si la solicitud HTTP fue exitosa o si ocurrió algún problema.
    Solicitud exitosa = 200
    No se encontro en el servidor la petición = 404
    Error interno dentro del servidor = 500
    """
        

if __name__ == "_main_":
    argparse_funcion()
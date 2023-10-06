"""
argparse Python:

La manera en la que se puede componer el manejo de esta librería es el siguiente:
#comando
#opciones
#argumentos

comando [opción] [argumento] -> puede variar si la opción requiere de un argumento o no.
Por ejemplo:
[*] En el sh cuando se utiliza el comando [ls] para ver una lista de los archivos y directorios se ejecuta sin nada más que el comando.
[*] Si se requiere ver los archivos ocultos en el directorio actual se le suma la [opción] -> ls -la -> comando [opción] -> este mismo no requiere de un argumento en específico.
[*] Pero si se quiere ver los archivos ocultos de un directorio en concreto, se le agrega él [argumento] -> ls -la /Desktop -> comando [opción] [argumento]

Este tipo de método se lo llama CLI [Command Line Interfaces]-> No es gráfico, sino que son una herramienta perfecta de la línea de comandos. 



"""
import argparse

def arg_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", '--numero_a', type=int , required=False ,default=0, help="Primer variable, valor por default 0, debe ingresar un numero")
    parser.add_argument("-b", '--numero_b', type=int , required=False ,default=0, help="Segunda variable, valor por default 0, debe ingresar un numero")
    parser.add_argument("-o", '--operacion',
                        type=str,
                        choices = ['suma','resta'],
                        default='suma', 
                        required=False,
                        help='Realiza una operacion de suma o resta')
    

    args = parser.parse_args()
    
    if args.operacion == 'suma':
        return print(args.numero_a + args.numero_b)
    elif args.operacion == 'resta':
        print(args.numero_a - args.numero_b)
    

arg_parser()
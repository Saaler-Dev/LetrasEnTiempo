import time
import sys
"""
colores:
VERDE = "\033[32m"
AZUL = "\033[34m"
CIAN = "\033[36m"
ROJO = "\033[31m"
MAGENTA = "\033[35m"
"""
MAGENTA = "\033[38;2;255;105;180m"
CIAN = "\033[38;2;0;191;255m"
RESET = "\033[0m"
AMARILLO = "\033[33m"
AZUL = "\033[38;2;0;191;255m"
VERDE = "\033[38;2;152;251;152m"
BLANCO = "\033[37m"
def cantar(texto, color, espera_final, velocidad=0.06, fin="\n"):
    sys.stdout.write(color)
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    
    sys.stdout.write(RESET + fin) 
    time.sleep(espera_final)

def prueba():

    cantar("I guess she's gotta ", BLANCO, 0.0, 0.05,fin="")
    cantar("CUT BLUE HAIR OFF",AZUL, 1.3, 0.05 )

def Letras():
    print(f"{MAGENTA}--- TV Girl: Blue Hair ---{RESET}\n")
    time.sleep(0.3)
    cantar("pam pam pam...", CIAN, 1.8, 0.13)
    cantar("pam pam pam...", CIAN, 2.0, 0.13)
    cantar("pam pam pam...", MAGENTA, 1.6, 0.13)
    cantar("pam pam pam...", MAGENTA, 2.8, 0.13)

    cantar("She asked me how to be funny", BLANCO, 1.5, 0.07)
    cantar("But that's not something you can teach", BLANCO, 0.8, 0.04)

    cantar("pam pam pam...", MAGENTA, 1.8, 0.13)
    cantar("pam pam pam...", MAGENTA, 1.0, 0.13)

    cantar("What seemed so ", BLANCO, 0.01, 0.06, fin="")
    cantar("blue ", AZUL,  0.0, 0.06,fin="")
    cantar("in the ", BLANCO,  0.0, 0.07,fin="")
    cantar("sunlight", AMARILLO,  2, 0.07)
    cantar("By the night was a ", BLANCO, 0.0, 0.07,fin="")
    cantar("pale green", VERDE,  1, 0.07)
    
    cantar("pam pam pam...", CIAN, 2.0, 0.13)
    cantar("pam pam pam...", MAGENTA, 0.8, 0.13)

    cantar("And I tried ", MAGENTA, 1.0, 0.05, fin="")
    cantar("to hold her", CIAN,  2.5, 0.10)
    cantar("But it didn't really last long", BLANCO, 1.1, 0.07)
    cantar("She's getting older", BLANCO, 2, 0.06)
    cantar("I guess she's gotta ", BLANCO, 0.0, 0.05, fin="")
    cantar("CUT BLUE HAIR OFF", AZUL, 1.3, 0.05 )


    cantar("pam pam pam...", CIAN, 1.8, 0.13)
    cantar("pam pam pam...", MAGENTA, 1.8, 0.13)
    cantar("pam pam pam...", CIAN, 1.4, 0.13)
    cantar("pam pam pam...", MAGENTA, 2.5, 0.13)

    cantar("She asked me if she was ", BLANCO, 0.0, 0.07, fin="")
    cantar("pretty", MAGENTA, 1.6, 0.07)
    cantar("Well, it's clear that the girl's a fraud", BLANCO, 1.0, 0.05)
    
    cantar("pam pam pam...", MAGENTA, 1.8, 0.13)
    cantar("pam pam pam...", MAGENTA, 1.0, 0.13)

    cantar("There's really no way of winning", BLANCO, 0.8, 0.07)
    cantar("If in their eyes you'll always be a dumb ", BLANCO, 0.0, 0.07,fin="")
    cantar("blonde", AMARILLO, 1.0, 0.07)
    
    cantar("pam pam pam...", MAGENTA, 1.8, 0.13)
    cantar("pam pam pam...", MAGENTA, 1.0, 0.13)

    cantar("And she cried over nothing", AMARILLO, 1.5, 0.08)
    cantar("So there was nothing I could do to stop", AMARILLO, 1.5, 0.06)
    cantar("Her from cutting", AMARILLO, 1.2, 0.08)
    cantar("Her beautiful blue hair off", CIAN, 1.0, 0.07)
    
    cantar("pam pam pam...", CIAN, 1.8, 0.13)
    cantar("pam pam pam...", MAGENTA, 1.8, 0.13)
    cantar("pam pam pam...", CIAN, 1.4, 0.13)
    cantar("pam pam pam...", MAGENTA, 2.5, 0.13)

    cantar("It looked like cotton candy", AMARILLO, 2.0, 0.08)
    cantar("And just as quick to get licked away", AMARILLO, 1.0, 0.07)
    
    cantar("pam pam pam...", MAGENTA, 1.8, 0.13)
    cantar("pam pam pam...", MAGENTA, 1.0, 0.13)

    cantar("Last I heard she was living", AMARILLO, 1.5, 0.08)
    cantar("With a boy who acts his age", AMARILLO, 1.0, 0.08)
    
    cantar("pam pam pam...", MAGENTA, 1.8, 0.13)
    cantar("pam pam pam...", MAGENTA, 1.0, 0.13)

    cantar("And I guess I'll just miss her", AMARILLO, 2.0, 0.08)
    cantar("Even though she isn't even really gone", AMARILLO, 1.5, 0.06)
    cantar("But things are just different", AMARILLO, 1.2, 0.08)
    cantar("Ever since she cut her blue hair off", AMARILLO, 2.0, 0.07)

if __name__ == "__main__":
    Letras()
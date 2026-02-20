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
MAGENTA = "\033[35m"
CIAN = "\033[36m"
RESET = "\033[0m"
AMARILLO = "\033[33m"

def cantar(texto, color, espera_final, velocidad=0.08):
    sys.stdout.write(color)
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad) 
    sys.stdout.write(RESET + "\n")
    time.sleep(espera_final)

def Letras():
    print(f"{MAGENTA}--- TV Girl: Blue Hair ---{RESET}\n")
    
    cantar("pam pam pam...", CIAN, 3.0)
    cantar("pam pam pam...", MAGENTA, 3.0)
    cantar("pam pam pam...", CIAN, 3.0)
    cantar("pam pam pam...", MAGENTA, 2.0)

    cantar("She asked me how to be funny", AMARILLO, 1.5, 0.08)
    cantar("But that's not something you can teach", AMARILLO, 1.0, 0.08)
    
    cantar("pam pam pam...", CIAN, 3.0)
    cantar("pam pam pam...", MAGENTA, 2.0)

    cantar("What seemed so blue in the sunlight", AMARILLO, 1.2, 0.07)
    cantar("By the night was a pale green", AMARILLO, 1.0, 0.07)
    
    cantar("pam pam pam...", CIAN, 3.0)
    cantar("pam pam pam...", MAGENTA, 2.0)

    cantar("And I tried to hold her", AMARILLO, 1.5, 0.09)
    cantar("But it didn't really last long", AMARILLO, 1.5, 0.08)
    cantar("She's getting older", AMARILLO, 1.2, 0.09)
    cantar("I guess she's gotta cut her blue hair off", CIAN, 1.0, 0.07)
    
    cantar("pam pam pam...", CIAN, 3.0)
    cantar("pam pam pam...", MAGENTA, 3.0)
    cantar("pam pam pam...", CIAN, 3.0)
    cantar("pam pam pam...", MAGENTA, 2.0)

    cantar("She asked me if she was pretty", AMARILLO, 1.5, 0.08)
    cantar("Well, it's clear that the girl's a fraud", AMARILLO, 1.0, 0.08)
    
    cantar("pam pam pam...", CIAN, 3.0)
    cantar("pam pam pam...", MAGENTA, 1.5)

    cantar("There's really no way of winning", AMARILLO, 1.2, 0.07)
    cantar("If in their eyes you'll always be a dumb blonde", AMARILLO, 1.0, 0.06)
    
    cantar("pam pam pam...", CIAN, 3.0)
    cantar("pam pam pam...", MAGENTA, 1.5)

    cantar("And she cried over nothing", AMARILLO, 1.5, 0.08)
    cantar("So there was nothing I could do to stop", AMARILLO, 1.5, 0.06)
    cantar("Her from cutting", AMARILLO, 1.2, 0.08)
    cantar("Her beautiful blue hair off", CIAN, 1.0, 0.07)
    
    cantar("pam pam pam...", CIAN, 3.0)
    cantar("pam pam pam...", MAGENTA, 3.0)
    cantar("pam pam pam...", CIAN, 3.0)
    cantar("pam pam pam...", MAGENTA, 2.0)

    cantar("It looked like cotton candy", AMARILLO, 2.0, 0.08)
    cantar("And just as quick to get licked away", AMARILLO, 1.0, 0.07)
    
    cantar("pam pam pam...", CIAN, 3.0)
    cantar("pam pam pam...", MAGENTA, 1.0)

    cantar("Last I heard she was living", AMARILLO, 1.5, 0.08)
    cantar("With a boy who acts his age", AMARILLO, 1.0, 0.08)
    
    cantar("pam pam pam...", CIAN, 3.0)
    cantar("pam pam pam...", MAGENTA, 1.5)

    cantar("And I guess I'll just miss her", AMARILLO, 2.0, 0.08)
    cantar("Even though she isn't even really gone", AMARILLO, 1.5, 0.06)
    cantar("But things are just different", AMARILLO, 1.2, 0.08)
    cantar("Ever since she cut her blue hair off", AMARILLO, 2.0, 0.07)

if __name__ == "__main__":
    Letras()
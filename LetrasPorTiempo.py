import time
import sys

MAGENTA = "\033[38;2;255;105;180m"
CIAN = "\033[38;2;0;191;255m"
RESET = "\033[0m"
AMARILLO = "\033[33m"
AZUL = "\033[38;2;0;191;255m"
VERDE = "\033[38;2;152;251;152m"
BLANCO = "\033[37m"

#Solamente tengo los colores mencionados arriba, si deseas aplicar algún color en las letras, sigue la siguiente estructura
# letra("parte de la canción", COLOR, tiempo entre mensaje, velocidad en la que saldrá la linea completa)
#en caso quieras que en esa linea tenga palabras de diferente color, puedes agregar fin = "" dentro de la estructura "letra(..., fin= "")"
#y para cerrar el ciclo, simplemente en la siguiente estructura no le agregue el fin="" -> Observa el def prueba

def letra(texto, color, tiempo, vel=0.06, fin="\n"):
    sys.stdout.write(color)
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(vel)
    
    sys.stdout.write(RESET + fin) 
    time.sleep(tiempo)

def prueba():

    letra("But if you're too drunk to drive", BLANCO, 0.6, 0.05, fin="")
    letra(" and the music is right", VERDE,  1.3, 0.07)
    letra("She might let you stay", BLANCO,  0.8, 0.06, fin="")
    letra(" but just for the night", AZUL,  0.5, 0.06)
    letra("And if she grabs for your hand", BLANCO, 0, 0.05,fin="")
    letra(" and drags you along", MAGENTA,  1, 0.07)

def Letras():

    print(f"{BLANCO}TV Girl - Lovers Rock\n")
    time.sleep(13)

    letra("Are you sick of me?", AMARILLO, 2.6, 0.09)
    letra("Would you like to be?", BLANCO, 1.5, 0.06)
    letra("I'm trying to tell you something", BLANCO, 2, 0.04)
    letra("Something that I already said", BLANCO, 5, 0.09)

    letra("You like a ", BLANCO, 0, 0.08, fin="")
    letra("pretty ", MAGENTA, 0, 0.08, fin="")
    letra("boy", BLANCO, 3, 0.08)
    
    letra("With a ", BLANCO, 0, 0.08, fin="")
    letra("pretty ", MAGENTA, 0, 0.08, fin="")
    letra("voice", BLANCO, 1, 0.08)

    letra("Who is trying to sell you something", BLANCO, 1.4, 0.05)
    letra("Something that you already have", BLANCO, 4.0, 0.08)

    letra("But if you're too drunk to drive", BLANCO, 0.6, 0.05 )
    letra("and the music is right", BLANCO,  1.3, 0.07)
    letra("She might let you stay", BLANCO,  0.8, 0.06)
    letra("but just for the night", BLANCO,  0.5, 0.06)
    letra("And if she grabs for your hand", BLANCO, 1.02, 0.05)
    letra("and drags you along", BLANCO,  1, 0.07)

    letra("She might want a kiss", BLANCO, 1.0, 0.06)
    letra("before the end of this song", BLANCO, 0.5, 0.06)

    letra("Because ", BLANCO, 0, 0.05, fin="")
    letra("love ", MAGENTA, 2.8, 0.05, fin="")
    letra("can burn like a", BLANCO, 0, 0.09, fin="")
    letra(" cigarette...", BLANCO, 3.0, 0.06)

    letra("And leave you with nothing", BLANCO, 2.5, 0.07)
    letra("And leave you with nothing", BLANCO, 3, 0.07)

def Letras1():

    print(f"{MAGENTA}TV Girl - Blue Hair\n")
    time.sleep(0.3)
    letra("pam pam pam...", CIAN, 1.8, 0.13)
    letra("pam pam pam...", CIAN, 2.0, 0.13)
    letra("pam pam pam...", MAGENTA, 1.6, 0.13)
    letra("pam pam pam...", MAGENTA, 2.8, 0.13)

    letra("She asked me how to be funny", BLANCO, 1.5, 0.07)
    letra("But that's not something you can teach", BLANCO, 0.8, 0.04)

    letra("pam pam pam...", MAGENTA, 1.8, 0.13)
    letra("pam pam pam...", MAGENTA, 1.0, 0.13)

    letra("What seemed so ", BLANCO, 0.01, 0.06, fin="")
    letra("blue ", AZUL,  0.0, 0.06,fin="")
    letra("in the ", BLANCO,  0.0, 0.07,fin="")
    letra("sunlight", AMARILLO,  2, 0.07)
    letra("By the night was a ", BLANCO, 0.0, 0.07,fin="")
    letra("pale green", VERDE,  1, 0.07)
    
    letra("pam pam pam...", CIAN, 2.0, 0.13)
    letra("pam pam pam...", CIAN, 0.8, 0.13)

    letra("And I tried ", MAGENTA, 1.0, 0.05, fin="")
    letra("to hold her", CIAN,  2.5, 0.10)
    letra("But it didn't really last long", BLANCO, 1.1, 0.07)
    letra("She's getting older", BLANCO, 2, 0.06)
    letra("I guess she's gotta ", BLANCO, 0.0, 0.05, fin="")
    letra("CUT BLUE HAIR OFF", AZUL, 1.3, 0.05 )


    letra("pam pam pam...", CIAN, 1.8, 0.13)
    letra("pam pam pam...", CIAN, 1.8, 0.13)
    letra("pam pam pam...", MAGENTA, 1.4, 0.13)
    letra("pam pam pam...", MAGENTA, 2.5, 0.13)

    letra("She asked me if she was ", BLANCO, 0.0, 0.07, fin="")
    letra("pretty", MAGENTA, 1.6, 0.07)
    letra("Well, it's clear that the girl's a fraud", BLANCO, 1.0, 0.05)
    
    letra("pam pam pam...", MAGENTA, 1.8, 0.13)
    letra("pam pam pam...", MAGENTA, 1.0, 0.13)

    letra("There's really no way of winning", BLANCO, 0.8, 0.07)
    letra("If in their eyes you'll always be a dumb ", BLANCO, 0.0, 0.07,fin="")
    letra("blonde", AMARILLO, 1.0, 0.07)
    
    letra("pam pam pam...", MAGENTA, 1.8, 0.13)
    letra("pam pam pam...", MAGENTA, 1.0, 0.13)

    letra("And she cried over nothing", AMARILLO, 1.5, 0.08)
    letra("So there was nothing I could do to stop", AMARILLO, 1.5, 0.06)
    letra("Her from cutting", AMARILLO, 1.2, 0.08)
    letra("Her beautiful blue hair off", CIAN, 1.0, 0.07)
    
    letra("pam pam pam...", CIAN, 1.8, 0.13)
    letra("pam pam pam...", MAGENTA, 1.8, 0.13)
    letra("pam pam pam...", CIAN, 1.4, 0.13)
    letra("pam pam pam...", MAGENTA, 2.5, 0.13)

    letra("It looked like cotton candy", AMARILLO, 2.0, 0.08)
    letra("And just as quick to get licked away", AMARILLO, 1.0, 0.07)
    
    letra("pam pam pam...", MAGENTA, 1.8, 0.13)
    letra("pam pam pam...", MAGENTA, 1.0, 0.13)

    letra("Last I heard she was living", AMARILLO, 1.5, 0.08)
    letra("With a boy who acts his age", AMARILLO, 1.0, 0.08)
    
    letra("pam pam pam...", MAGENTA, 1.8, 0.13)
    letra("pam pam pam...", MAGENTA, 1.0, 0.13)

    letra("And I guess I'll just miss her", AMARILLO, 2.0, 0.08)
    letra("Even though she isn't even really gone", AMARILLO, 1.5, 0.06)
    letra("But things are just different", AMARILLO, 1.2, 0.08)
    letra("Ever since she cut her blue hair off", AMARILLO, 2.0, 0.07)

if __name__ == "__main__":
    prueba()
from hmac import digest
from pickle import TRUE
import random 
#Accedimos a la base de datos de las palabras.
def read(data_read="/home/juarez2112/juego/data.txt"):
    word=[]
    with open(data_read,"r",encoding="utf-8") as f:
        for letter in f:
            word.append(letter.strip().upper())
    return word 
    '''Usamos return word porque aparece el error:
    TypeError: object of type 'NoneType' has no len()
    Los errores comunes que pueden causar este error son:

    Reasignación de una lista con una función integrada
    Olvidarse de incluir una instrucción return en una función
    '''
def run():
    '''Utilizaremos la libreria random
    lo que hara es usar de la base de datos de data (donde almacena las palabras)
    es que imprima una palabra random. '''
    data=read(data_read="/home/juarez2112/juego/data.txt")
    random_word=random.choice(data)#Palabra al azar de la base de datos
    letra_ancho=[letra for letra in random_word]#crea una lista de la palbra
    random_hide=["*"] * len(letra_ancho)#usa len para el largo de la palabra.
    print(random_hide)
    digita_palabra=input("Digita una palabra: ")
    digita_palabra=digita_palabra.upper().strip()
    assert digita_palabra.isalpha(), "No se admiten Numeros"
    if digita_palabra == random_word:
        print('si es la palabra')
    else: 
        print(f"No es la palabra.")
    
    print("Hola")    
    
if __name__=="__main__":
    run()
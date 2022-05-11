from ctypes.wintypes import WORD
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
    random_word=random.choice(data)
    print(random_word)
    
if __name__=="__main__":
    run()
import random
import os
def run():
    data=["nariz","nube","animal","carro","pez","arma","luna","tren","brazo","perro", "gato","cuaderno","elefante","chocolate","pulpo","ingles","agua","mexico"]
    word=random.choice(data)
    phrase_random=[]#Palabra random almacenada como una lista.
    for x in word:
        phrase_random.append(x.upper().strip())
    under_score=["_"]*len(phrase_random)
    print(under_score)
    
    letras=input("Introduce una letra: ")
    frase=[]
    for letra in frase:
        frase.append(letras)
    print(letra)

if __name__=='__main__':
    run()
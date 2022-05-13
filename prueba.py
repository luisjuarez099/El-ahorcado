import random
def run():
    data=["nariz","nube","animal","carro","pez","arma","luna","tren","brazo","perro", "gato"]
    word=random.choice(data)
    phrase_random=[]#Palabra random almacenada como una lista. para comparar. 
    for x in word:
        phrase_random.append(x.upper().strip())
    #print(phrase_random)

    #--------------------Me oculta la palabra que debo de adivinar.
    for letter in word:
        #print(ord(letter.upper()),end="->")
        for i in letter:
            i=i.upper()
            print(["__"],end=" ".upper().strip())
    #Imprime el largo de la palabra que debo de digitar sus letras.
    print(" ")    

    frase=[]#Se almacena la palabra que vamos a introducir.
    for i in word:
        frase.append(input("Introduce una palabra: ").upper().strip())
    # for j in frase:#Imprime cada palabra su codigo ascii
    #     print(ord(j),end=" ")
    print(frase)

    
    #Para comparar podremos usar codigo ASCII????
    # print(phrase_random)
    # print(frase)
    # if set(phrase_random)==set(frase):
    #     print("Son iguales")
    # else:
    #     print("No son iguales")
    #     print(f"La palabra era: {phrase_random}")
    
   
if __name__=='__main__':
    run()
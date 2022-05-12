import random
data=["nariz","nube","animal","carro","pez","arma","luna","tren","brazo","perro", "gato","chcolate","navidad","elefante","dentista"]
word=random.choice(data)

def run():
    phrase_random=[letra for letra in word.upper().strip()]
    print(phrase_random)

    



if __name__=='__main__':
    run()
    

    


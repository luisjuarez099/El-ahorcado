import random
data=["nariz","nube","animal","carro","pez","arma","luna","tren","brazo","perro", "gato"]
word=random.choice(data)
print(word.upper().strip())

for letter in word:
    #print(letra, end=" ")
    hide_word=["_"]*len(letter)
    print(hide_word,end=" ".strip().upper())
    
    


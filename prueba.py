import random

DATA=["perro","pavo","iguana","navidad","regalos","piernas","playa","tiburon","serpiente","ojo","salamandra","cocodrilo","amistad","padres","perico","analisis","ropa","gucci","adidas","lululemon","aeropostal"]

random_palabra=random.choice(DATA)
lista_random_palabra=[letra for letra in random_palabra]#se gurda en la lista la palabra una palabra  random. 

lista_random_palabra=["_"]*len(lista_random_palabra)#Imprime oculto la palabra random.
lista_letras_anadidas=[]#se gurda palabras que el usuario va almacenando

while True:
    recolector_letra=""
    print(f"Palabra para adivinar: {lista_random_palabra}")
    digitar_letras=input("Digita una letra: ")
    lista_letras_anadidas.append(digitar_letras)
    for letter in lista_random_palabra:
        if letter in lista_letras_anadidas:
            print("Si es la palabra")
            recolector_letra+=letter




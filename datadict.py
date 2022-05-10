def read():
    letter=[]
    with open("/home/juarez2112/juego/data.txt","r",encoding="utf-8") as f:
        for line in f:
            letter.append(line)
    print(letter)

def write():
    pass
    # names=["luis","pepe","Jose","Alberto","Zara"]
    # with open("./archivos/names.txt","w",encoding="utf-8") as f:
    #     for name in names:
    #         f.write(name)
    #         f.write("\n")
def run():
    read()


if __name__ == '__main__':
    run()
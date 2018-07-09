import random

def jogar():

    imprime_abertura()
    palavra_secreta = carrega_palavra_secreta()
    #palavra_secreta = "maça".upper()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou  = False
    erros    = 0

    while(not enforcou and not acertou):
        chute = input("Entre uma letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                    print("Encontrei a letra {} na posição {}".format(letra, index))
                index += 1
            
        else:
            erros += 1

        print (letras_acertadas)
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
    
    if (acertou):
        print ("Você ganhou!!!!!")
    else:
        print ("Você perdeu...")
    print ("Fim do jogo!")




def imprime_abertura():
    print ("*******************************")
    print ("Bem vindo ao jogo de Forca")
    print ("*******************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


if(__name__=="__main__"):
    jogar()
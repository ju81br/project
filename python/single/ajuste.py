# sergio fonseca
# 17/06/2018
# ler arquivo e inserir aspas simples e virgula nos registros lidos
arquivo = open('lista.txt', 'r')
escreve = open('nova.txt', 'w')

aspas = "%s" %("'")
virgula = "%s" %(",")
contador = 0

for linhas in arquivo:
    contador = contador + 1
    linhas = linhas.rstrip()
    linhas = aspas + linhas + aspas + virgula
    #linhas = "{0}{1}{2}{3}" .format (aspas, linhas, aspas, virgula)
    escreve.write(linhas + "\n")
    #print (linhas)
#escreve.write(linhas[-50:-1].replace(",", ""))

print ('----------------------------------------')
print ('Registros lidos: ' + str(contador))
print ('----------------------------------------')
escreve.close()
arquivo.close()

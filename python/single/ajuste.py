# sergio fonseca
# 17/06/2018
# ler arquivo e inserir aspas simples e virgula nos registros lidos
arquivo = open('lista.txt', 'r')
escreve = open('nova.txt', 'w')

aspas = "%s" %("'")
virgula = "%s" %(",")
contador = 0

total = sum(1 for linha in arquivo)
arquivo.seek(0)

for linhas in arquivo:
    contador += 1
    linhas = linhas.rstrip()
    if not contador != total:
        linhas = aspas + linhas + aspas
    else:    
        linhas = aspas + linhas + aspas + virgula

    escreve.write(linhas + "\n")

print ('----------------------------------------')
print ('Registros lidos: ' + str(contador))
print ('----------------------------------------')
escreve.close()
arquivo.close()
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
total = contador
contador = 0
arquivo.seek(0)

for linhas in arquivo:
    contador = contador + 1
    linhas = linhas.rstrip()
    while contador != total:
        linhas = aspas + linhas + aspas + virgula
        break
    linhas = aspas + linhas + aspas # Ultimo registro sem a virgula
    escreve.write(linhas + "\n")

print ('----------------------------------------')
print ('Registros lidos: ' + str(contador))
print ('----------------------------------------')
escreve.close()
arquivo.close()

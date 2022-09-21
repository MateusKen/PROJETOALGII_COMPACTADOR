'''
NOME: Mateus Kenzo Iochimoto TIA: 32216289
NOME: Rodrigo Machado de Assis Oliveira de Lima TIA: 32234678
'''
arquivo_L = open('texto.txt', 'r')
arquivo_E = open('compactado.txt', 'w')
tam = len(arquivo_L.readlines())
arquivo_L.seek(0)

def conferePalavra(palavra, lista):
    for i in range(len(lista)):
        if lista[i] == '':
            break
        else:
            if palavra == lista[i]:
                return i
    return -1

def moveVetor(indice, palavra, lista):
    tamFila = 0
    for i in range(len(lista)):
        if lista[i] == '':
            tamFila = i
            print(tamFila)
            break
    if indice == -1:
        for i in range(tamFila, 0, -1):
            lista[i] = lista[i-1]
        lista[0] = palavra
        return lista
    else:
        palavraRepetida = lista[indice]
        for i in range(indice, 0, -1):
            lista[i] = lista[i-1]            
        lista[0] = palavra
        return lista

vetLinhas = ['']*tam #vetor com cada linha e suas palavras

for i in range(tam): 
    linha = arquivo_L.readline()
    linha = linha.rstrip()
    vetLinha = linha.split(' ')
    vetLinhas[i] = vetLinha

palavras = ['']*1000

for i in range(len(vetLinhas)):
    for j in range(len(vetLinhas[i])):
        estar = conferePalavra(vetLinhas[i][j], palavras)
        if estar == -1:
            #insere palavra na lista de palavras
            moveVetor(estar, vetLinhas[i][j], palavras)
            #escreve no arquivo palavra
            arquivo_E.write(vetLinhas[i][j])
            arquivo_E.write(" ")
        else:
            #muda a posicao da palavra repetida para 1ª posicao
            moveVetor(estar, vetLinhas[i][j], palavras)
            #escreve índice da palavra repetida
            arquivo_E.write(str(estar+1))
            arquivo_E.write(" ")
    arquivo_E.write('\n')

arquivo_L.close()
arquivo_E.close()

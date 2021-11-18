def verifica( caracter, matriz, aux ):
    for i in range(len(matriz)):
        if ( caracter == matriz[i][0] ):
            aux = int(matriz[i][aux])
    return (aux + 1)
            
def main():
    arq = open('tabelaLFA.txt', 'r')  #abre o arquivo
    texto = []  
    matriz = [] 
    texto = arq.readlines() #quebra as linhas do arquivo em vetores

    for i in range(len(texto)):          
        matriz.append(texto[i].split(";"))  
    arq.close() 

    arq2 = open('entrada.txt', 'r')
    texto2 = []
    texto2 = arq2.readline()
    aux2 = []

    aux2 = texto2.split(" ")
    arq2.close()

    aux = 1   
    for x in aux2:
        for i in range(len(x)):
            aux = verifica( x[i], matriz, aux )
        
        print(matriz[47][aux])
        aux = 1

main()
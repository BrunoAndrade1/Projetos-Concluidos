''' Função LeiaMatriz '''

def LeiaMatriz():
    # Lê e retorna uma matriz contendo todas as apostas da megasena.
    # Cada linha contém:
        # mat[][0] - int - número do sorteio
        # mat[][1] - str - data do sorteio
        # mat[][2..7] - int - cada dezena sorteada (1 a 60)
    # Retorna None se houve algum erro na leitura.
    mat = [] # inicia a matriz
    # abrir o arquivo para leitura
    try:
        arq = open('megasena.txt', "r")
    except:
        print("Erro na abertura do arquivo (open)")
        return None
    # ler cada uma das linhas do arquivo
    i = 0
    for line in arq:
        # se der alguma exception retorna None
        try:
            lin = line[:len(line) - 1] # tira o \n do final
            v = lin.split()# separa os elementos da string
            mat.append([]) # adiciona uma nova linha a matriz
            # Transforma os strings numéricos em números inteiros
            for j in range(8):
                if j == 1:
                    mat[i].append(v[1])
                else:
                    mat[i].append(int(v[j]))
            i = i + 1
        except:
            # algum erro no trecho acima
            print("Erro no split(), no int() ou no append()")
            return None

    for i in range(len(mat)):
        for k in range(2,8):
            if not 1 <= mat[i][k] <= 60:
                print("Fora do intervalo")
                return

    # fechar arquivo e retornar a matriz
    arq.close()
    return mat


def MegasenaA():
    n = []
    cont = 0
    print("Numeros que mais vezes foram sorteados:")
    matriz = LeiaMatriz()
    for a in range(1,61):
        n.append([])
        for b in range(len(matriz)):
            for c in range(2,8):
                if a == matriz[b][c]:
                    cont += 1
        n[a-1].append(a)
        n[a-1].append(cont)
        cont = 0
    for d in range(1, len(n)):
        while d>0 and n[d][1] < n[d-1][1]:
            n[d], n[d-1] = n[d-1], n[d]
            d -= 1
    n.reverse()
    print("Número        Sorteio")
    for f in range(len(n)):
        print('%2d'%n[f][0], '%14d'%n[f][1])
    print("\n")

def MegasenaB():
    n = []
    cont = 0
    print("Numeros que menos vezes foram sorteados:")
    matriz = LeiaMatriz()
    for a in range(1,61):
        n.append([])
        for b in range(len(matriz)):
            for c in range(2,8):
                if a == matriz[b][c]:
                    cont += 1
        n[a-1].append(a)
        n[a-1].append(cont)
        cont = 0
    for d in range(1, len(n)):
        while d>0 and n[d][1] < n[d-1][1]:
            n[d], n[d-1] = n[d-1], n[d]
            d -= 1
    n.reverse()
    print("Número        Sorteio")
    for f in range(len(n)-1, -1, -1):
        print('%2d'%n[f][0], '%14d'%n[f][1])
    print("\n")
    
def MegasenaC():
    n = []
    cont = 0
    print("Numeros que a mais tempo não são sorteados:")
    print("Número      Sorteio    Data")
    matriz = LeiaMatriz()
    for i in range(len(matriz)):
        for j in range(2,8):
            if matriz[i][j] in n:
                pass
            else:
                n.append(matriz[i][j])
                n.append([matriz[i][0],matriz[i][1]])
    for i in range(len(n)-1,0, - 2):
        print("%2d%14d%17s"%(n[i-1],n[i][0],n[i][1]))
    print("\n")    

def MegasenaD():
    n = []
    cont = 0
    print("Numeros que a menos tempo foram sorteados:")
    print("Número      Sorteio    Data")
    matriz = LeiaMatriz()
    for i in range(len(matriz)):
        for j in range(2,8):
            if matriz[i][j] in n:
                pass
            else:
                n.append(matriz[i][j])
                n.append([matriz[i][0],matriz[i][1]])
    for i in range(0,len(n),2):
        print("%2d%14d%17s"%(n[i],n[i+1][0],n[i+1][1]))
    print("\n")

MegasenaA()
MegasenaB()
MegasenaC()
MegasenaD()

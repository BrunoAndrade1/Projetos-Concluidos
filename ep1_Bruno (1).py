import urllib.request
import time
num_soluçoes = 0
num_sol_errada = 0

def LeiaMatrizRemota(NomeArquivo):
    '''Importa o arquivo e converte em uma lista'''

    # retorna True se conseguiu ler o arquivo e False caso contrário
    # abrir o arquivo para leitura
    try:
        urlarq = "http://www.ime.usp.br/~mms/mac1222s2019/" + NomeArquivo
        arq = urllib.request.urlopen(urlarq)
    except:
        return []  # retorna lista vazia se der erro

    # inicia matriz SudoKu a ser lida
    mat = [9 * [0] for k in range(9)]
    # ler todo o arquivo e separar em linhas
    arqtotal = arq.read()
    linhas = arqtotal.splitlines()
    # tratar cada uma das linhas do arquivo
    i = 0
    for linha in linhas:
        if len(linha) == 0:
            continue 
        v = linha.split()
        # verifica se tem 9 elementos e se são todos entre '1' e '9'
        try:
            if len(v) != 9:
                raise ('error')
            # transforma de texto para int
            for j in range(len(v)):
                mat[i][j] = int(v[j])
                if mat[i][j] < 0 or mat[i][j] > 9:
                    raise ('error')
            i += 1
        except:
            return False

    # fecha arquivo e retorna matriz lida e consistida
    arq.close()
    return mat

def Sudoku(mat, i = 0, j = 0):
     
    global num_soluçoes
    global num_sol_errada
    verificador = 0
    
    for l in range (9):
        if verificador == 1:
            break
        for c in range(9):
            if mat[l][c] == 0:
                linha = l
                coluna = c
                verificador += 1
                break

    if verificador == 0:
        if not TestaMatrizPreenchida(mat):# testa a matriz lida chamando a função
             print ()
             return
            
        num_soluçoes += 1
        print ("**** Matriz Completa ****")
        ImprimaMatriz(mat)#Imprime a matriz chamando a função        
                                         
        return    

    for numero in range(1,10):
        if verifica (mat,linha,coluna,numero):
            mat[linha][coluna]= numero
            Sudoku(mat,linha,coluna)
                      
    mat[linha][coluna] = 0
    return 

def verifica (mat, i, j, numero):# verifica se não Ha elementos repetidos na linha e coluna e no quadrado interno 
    for x in range(9):
         if x != i:
        
            if mat[x][j] == numero :
                return False
    for x in range(9):
         if x != j:
        
            if mat[i][x] == numero :
                return False
            
    sx =(i//3)*3
    sy =(j//3)*3

    for x in range(sx,sx + 3):
        for y in range(sy,sy+3):
            if not (x == i and y == j):
                if mat[x][y] == numero:
                    return False
                                                           
    return  True

def ImprimaMatriz(mat):
    for k in range(9):
        print(mat[k])
    print('\n')
    
def TestaMatrizPreenchida(mat):
    for i in range(9):
        for j in range(9):
            a = mat[i][j]
            if mat[i][j]  != 0:
                if not verifica(mat,i,j,a): return False
    return True

def main():
    global num_soluçoes

    while True:
       
        num_soluçoes = 0
         
        try:
            print('\nDigite 0 para sair')
            sudoku_a_ser_lido = int(input('Entre com numero do sudoku de 1 a 15  : '))
            a = sudoku_a_ser_lido
            if sudoku_a_ser_lido == 0:
                return
            if not 1 <= a <= 15:
                raise print('fora do intervalo')
            
        except :
            print( '\n************** Erro *****************')
            continue             
        
        time1 = time.time()
        arquivo = "sudoku" + str(sudoku_a_ser_lido)
        
        novo = (LeiaMatrizRemota(arquivo))    
        if novo == False:
            print ('\nErro na etapa LeiaMatrizRemota')      
            print ("Matriz Inconsistente")      
            continue
        
        print('\n     Matriz inicial     \n')
        ImprimaMatriz(novo)
        
        Sudoku(LeiaMatrizRemota(arquivo))

        time2=time.time()
        tempo_tot = time2-time1
        if num_soluçoes == 0:
            
            print('  Matriz Incompleta')
            print('****************************')
        
        print('tempo de solucão foi em segundos ',tempo_tot)
        print( 'o numero de solucoes é ',num_soluçoes)
        
        
        
        
                          
    
    

main()


    

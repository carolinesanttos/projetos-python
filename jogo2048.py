# PROJETO EM ANDAMENTO

#Componente Curricular: Algoritmos I
#Concluído em: 00/00/2023
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
#código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

from random import randint

# Função que gera números aleatórios para linha e coluna
def geraNumeros():
    linha = randint(0,3)
    coluna = randint(0,3)
    return linha, coluna

# Recebe números aleatórios para por em posições aleatórias no tabuleiro o número 2
def colocaNumAleatorio(tabuleiro):
    x = True
    y = True
    # Esse while se repete até que um número aleatório encontre uma posição vazia no tabuleiro
    while x == True:
        i=0
        l1, c1 = geraNumeros()
        l2, c2 = geraNumeros()
        
        if tabuleiro[l1][c1] == 0:
            tabuleiro[l1][c1] = 2
            x = False
            
    while y == True:
        for l in range (0, 4):
            for c in range (0,4):
                if (tabuleiro[l][c] != 0):
                    i+=1     
        # A condição abaixo serve para anular as posições iguais, pois devem estar em posições diferentes
        if (l1 == l2) and (c1 == c2):
            l2, c2 = geraNumeros()
        elif (l1 != l2) or (c1 != c2):
            y = False
    # Esse elif serve para verificar se foram colocados os dois números no tabuleiro no inicio do jogo
    # Se ele for diferente de um, quer dizer que ele não precisa mais aparecer no tabuleiro
    if (i == 1):
        tabuleiro_origem[l2][c2] = 2
        
        
# Cria tabuleiro original
def tabuleiroOriginalZerado (tabuleiro):
    print()
    for l in range (0, 4):
        for c in range (0,4):
            print(f'[{tabuleiro[l][c]:^5}]', end = '')
        print()
    print()


def menu ():
    print('-='*20)
    print("Welcome to the game 2048.")
    print("1. Start")
    print("2. Exit")
    print("Escolha a opção [1] para começar e [2] para sair.")
    resp = int(input('> '))
    print('-='*20)
    return resp
    

# Menu para escolha de movimento dos blocos no tabuleiro
def menuMovimentos ():
    print("Para qual posição deseja mover os blocos?")
    print('1. Para cima')
    print('2. Para baixo')
    print('3. Para esquerda')
    print('4. Para direita')
    print('Escolha uma das opções [1-4]:')


# Função responsável por movimentar o tabuleiro para cima, baixo, esquerda e direita
def movimentandoBlocos (tabuleiro, escolha):
    # Movimento para cima
    if (escolha == 1):
        print('\n=======PARA CIMA=======\n')
        # Percorrendo a matriz para saber se existe algum espaço para colocar o número na posição desejada
        for l in range (0,4):
            for c in range (0,4):
                # Se achar um número diferente de 0 na coluna da linha anterior, ele coloca o valor na coluna da linha anterior
                if (tabuleiro[l][c] != 0):
                    if l == 1:
                        if (tabuleiro[l-1][c]) == 0:
                            tabuleiro[l-1][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                                                            
                    elif l == 2:
                        if (tabuleiro[l-2][c] == 0) and (tabuleiro[l-1][c] == 0):
                            tabuleiro[l-2][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l-1][c] == 0):
                            tabuleiro[l-1][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                                                    
                    elif l == 3:
                        if (tabuleiro[l-3][c] == 0) and (tabuleiro[l-2][c] == 0) and (tabuleiro[l-1][c] == 0):
                            tabuleiro[l-3][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l-2][c] == 0) and (tabuleiro[l-1][c] == 0):
                            tabuleiro[l-2][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l-1][c] == 0):
                            tabuleiro[l-1][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        
                    # Soma valores idênticos
                    somaNumerosIdenticos(tabuleiro, l, c, escolha)
                           
    # Movimento para baixo                    
    elif (escolha == 2):
        print('\n=======PARA BAIXO=======\n') 
        # Percorrendo a matriz para saber se existe algum espaço para colocar o número na posição desejada
        for l in range (3,-1,-1):
            for c in range (3,-1,-1):
                if (tabuleiro[l][c] != 0):
                    
                    if l == 0:
                        if (tabuleiro[l+3][c] == 0) and (tabuleiro[l+2][c] == 0) and (tabuleiro[l+1][c] == 0):
                            tabuleiro[l+3][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                            
                        elif (tabuleiro[l+2][c] == 0) and (tabuleiro[l+1][c] == 0):
                            tabuleiro[l+2][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                            
                        elif (tabuleiro[l+1][c] == 0):
                            tabuleiro[l+1][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                            
                    elif l == 1:
                        if (tabuleiro[l+2][c] == 0) and (tabuleiro[l+1][c] == 0):
                            tabuleiro[l+2][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                            
                        elif (tabuleiro[l+1][c] == 0):
                            tabuleiro[l+1][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                    
                    elif l == 2:
                        if (tabuleiro[l+1][c]) == 0:
                            tabuleiro[l+1][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                    # Soma valores idênticos            
                    somaNumerosIdenticos(tabuleiro, l, c, escolha)
                
    # Movimento para esquerda            
    elif (escolha == 3):
        # Percorrendo a matriz para saber se existe algum espaço para colocar o número na posição desejada
        print('\n=======PARA ESQUERDA=======\n') 
        for l in range (0,4):
            for c in range (0,4):
                if (tabuleiro[l][c] != 0):
                    
                    if c == 1:
                        if (tabuleiro[l][c-1]) == 0:
                            tabuleiro[l][c-1] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                                                            
                    elif c == 2:
                        if (tabuleiro[l][c-1] == 0) and (tabuleiro[l][c-2] == 0):
                            tabuleiro[l][c-2] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                            
                        elif (tabuleiro[l][c-1] == 0):
                            tabuleiro[l][c-1] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                                                    
                    elif c == 3:
                        if (tabuleiro[l][c-3] == 0) and (tabuleiro[l][c-2] == 0) and (tabuleiro[l][c-1] == 0):
                            tabuleiro[l][c-3] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l][c-2] == 0) and (tabuleiro[l][c-1] == 0):
                            tabuleiro[l][c-2] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l][c-1] == 0):
                            tabuleiro[l][c-1] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        
                    # Soma valores idênticos
                    somaNumerosIdenticos(tabuleiro, l, c, escolha)
                    
    # Movimento para direita     
    elif (escolha == 4):
        # Percorrendo a matriz para saber se existe algum espaço para colocar o número na posição desejada
        print('\n=======PARA DIREITA=======\n') 
        for l in range (3,-1,-1):
            for c in range (3,-1,-1):
                if (tabuleiro[l][c] != 0):

                    if c == 0:
                        if (tabuleiro[l][c+3] == 0) and (tabuleiro[l][c+2] == 0) and (tabuleiro[l][c+1] == 0):
                            tabuleiro[l][c+3] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l][c+2] == 0) and (tabuleiro[l][c+1] == 0):
                            tabuleiro[l][c+2] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l][c+1] == 0):
                            tabuleiro[l][c+1] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                            
                    elif c == 1:
                        if (tabuleiro[l][c+2] == 0) and (tabuleiro[l][c+1] == 0):
                            tabuleiro[l][c+2] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l][c+1] == 0):
                            tabuleiro[l][c+1] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                    
                    elif c == 2:
                        if (tabuleiro[l][c+1]) == 0:
                            tabuleiro[l][c+1] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                            
                    # Soma valores idênticos        
                    somaNumerosIdenticos(tabuleiro, l, c, escolha)

def somaNumerosIdenticos (tabuleiro, l, c, escolha):
    soma = 0
    # Soma para cima
    if escolha == 1:
        if l == 1:
            if (tabuleiro[l-1][c] == tabuleiro[l][c]):
                soma = tabuleiro[l-1][c] + tabuleiro[l][c]
                tabuleiro[l-1][c] = soma
                tabuleiro[l][c] = 0
                
        elif l == 2:
            if (tabuleiro[l-2][c] == tabuleiro[l-1][c]):  
                soma = tabuleiro[l-2][c] + tabuleiro[l-1][c]
                tabuleiro[l-2][c] = soma
                tabuleiro[l-1][c] = 0 
                
            elif (tabuleiro[l][c] == tabuleiro[l-1][c]):
                soma = tabuleiro[l][c] + tabuleiro[l-1][c]
                tabuleiro[l-1][c] = soma
                tabuleiro[l][c] = 0   
                
        elif l == 3:
            if (tabuleiro[l-3][c] == tabuleiro[l-2][c]):
                soma = tabuleiro[l-3][c] + tabuleiro [l-2][c]
                tabuleiro[l-3][c] = soma
                tabuleiro [l-2][c] = 0 
                
            elif (tabuleiro[l-2][c] == tabuleiro[l-1][c]):
                soma = tabuleiro[l-2][c] + tabuleiro [l-1][c]
                tabuleiro[l-2][c] = soma
                tabuleiro [l-1][c] = 0 
                
            elif (tabuleiro[l][c] == tabuleiro[l-1][c]):
                soma = tabuleiro[l][c] + tabuleiro[l-1][c]
                tabuleiro[l-1][c] = soma
                tabuleiro[l][c] = 0       
                
    # Soma para baixo    
    elif escolha == 2:  
        if l == 0:
            if (tabuleiro[l+3][c] == tabuleiro[l+2][c]):
                soma = tabuleiro[l+3][c] + tabuleiro[l+2][c]
                tabuleiro[l+3][c] = soma
                tabuleiro[l+2][c] = 0
            
            elif (tabuleiro[l+2][c] == tabuleiro[l+1][c]):
                soma = tabuleiro[l+1][c] + tabuleiro[l+2][c]
                tabuleiro[l+2][c] = soma 
                tabuleiro[l+1][c] = 0
                
            elif (tabuleiro[l][c] == tabuleiro[l+1][c]):
                soma = tabuleiro[l][c] + tabuleiro[l+1][c]
                tabuleiro[l+1][c] = soma
                tabuleiro[l][c] = 0
                
        elif l == 1:
            if (tabuleiro[l+1][c] == tabuleiro[l+2][c]):
                soma = tabuleiro[l+1][c] + tabuleiro[l+2][c]
                tabuleiro[l+2][c] = soma
                tabuleiro[l+1][c] = 0
                
            elif (tabuleiro[l][c] == tabuleiro[l+1][c]):
                soma = tabuleiro[l][c] + tabuleiro[l+1][c]
                tabuleiro[l+1][c] = soma
                tabuleiro[l][c] = 0
                
        elif l == 2:
            if (tabuleiro[l][c] == tabuleiro[l+1][c]):
                soma = tabuleiro[l][c] + tabuleiro[l+1][c]
                tabuleiro[l+1][c] = soma
                tabuleiro[l][c] = 0
                
    # Soma para esquerda
    elif escolha == 3:
        if c == 1:
            if (tabuleiro[l][c-1] == tabuleiro[l][c]):
                soma = tabuleiro[l][c-1] + tabuleiro[l][c]
                tabuleiro[l][c-1] = soma
                tabuleiro[l][c] = 0
                
        elif c == 2:
            if (tabuleiro[l][c-2] == tabuleiro[l][c-1]):  
                soma = tabuleiro[l][c-2] + tabuleiro[l][c-1]
                tabuleiro[l][c-2] = soma
                tabuleiro[l][c-1] = 0 
                
            elif (tabuleiro[l][c-1] == tabuleiro[l][c]):
                soma = tabuleiro[l][c-1] + tabuleiro[l][c]
                tabuleiro[l][c-1] = soma
                tabuleiro[l][c] = 0   
                
        elif c == 3:
            if (tabuleiro[l][c-3] == tabuleiro[l][c-2]):
                soma = tabuleiro[l][c-3] + tabuleiro [l][c-2]
                tabuleiro[l][c-3] = soma
                tabuleiro [l][c-2] = 0 
                
            elif (tabuleiro[l][c-2] == tabuleiro[l][c-1]):
                soma = tabuleiro[l][c-2] + tabuleiro [l][c-1]
                tabuleiro[l][c-2] = soma
                tabuleiro [l][c-1] = 0 
                
            elif (tabuleiro[l][c-1] == tabuleiro[l][c]):
                soma = tabuleiro[l][c-1] + tabuleiro[l][c]
                tabuleiro[l][c-1] = soma
                tabuleiro[l][c] = 0
                
    # Soma para direita   
    elif escolha == 4:
        if c == 0:
            if (tabuleiro[l][c+3] == tabuleiro[l][c+2]):
                soma = tabuleiro[l][c+2] + tabuleiro[l][c+3]
                tabuleiro[l][c+3] = soma
                tabuleiro[l][c+2] = 0
            
            elif (tabuleiro[l][c+2] == tabuleiro[l][c+1]):
                soma = tabuleiro[l][c+2] + tabuleiro[l][c+1]
                tabuleiro[l][c+2] = soma 
                tabuleiro[l][c+1] = 0
                
            elif (tabuleiro[l][c+1] == tabuleiro[l][c]):
                soma = tabuleiro[l][c] + tabuleiro[l][c+1]
                tabuleiro[l][c+1] = soma
                tabuleiro[l][c] = 0
                
        elif c == 1:
            if (tabuleiro[l][c+2] == tabuleiro[l][c+1]):
                soma = tabuleiro[l][c+2] + tabuleiro[l][c+1]
                tabuleiro[l][c+2] = soma
                tabuleiro[l][c+1] = 0
                
            elif (tabuleiro[l][c+1] == tabuleiro[l][c]):
                soma = tabuleiro[l][c+1] + tabuleiro[l][c]
                tabuleiro[l][c+1] = soma
                tabuleiro[l][c] = 0
                
        elif c == 2:
            if (tabuleiro[l][c+1] == tabuleiro[l][c]):
                soma = tabuleiro[l][c+1] + tabuleiro[l][c]
                tabuleiro[l][c+1] = soma
                tabuleiro[l][c] = 0
        
        
        
        
        
        
        
        
# Programa principal
tabuleiro_origem =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
opcao = 0


opcao = menu()

while (opcao != 2): 
    
    if opcao == 1:
        
        colocaNumAleatorio(tabuleiro_origem)
        
        menuMovimentos()
        
        tabuleiroOriginalZerado(tabuleiro_origem)
        
        escolha = int(input('> '))
        
        movimentandoBlocos(tabuleiro_origem, escolha)
        
        
        
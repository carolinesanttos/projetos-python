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


# Cria tabuleiro original
def tabuleiroOriginalZerado (tabuleiro):
    for l in range (0, 4):
        for c in range (0,4):
            print(f'[{tabuleiro[l][c]:^5}]', end = '')
        print()


def menu ():
    print("""\n
          Welcome to the game 2048.
          1. Start
          2. Exit
          Escolha a opção [1] para começar e [2] para sair.
          """)

    resp = int(input('> '))
    return resp
    

# Menu para escolha de movimento dos blocos no tabuleiro
def menuMovimentos ():
    print(""""\n
          Para qual posição deseja mover os blocos?
          1. Para cima
          2. Para baixo
          3. Para esquerda
          4. Para direita
          Escolha uma das opções [1-4]:""")
    resp = int(input('> '))
    return resp


#
def movimentandoBlocos (tabuleiro):
    escolha = menuMovimentos()
    # Movimento para cima
    if (escolha == 1):
        # Percorrendo a matriz para saber se existe algum número para trocá-lo de posição
        for l in range (0,4):
            for c in range (0,4):
                # Se achar um número diferente de 0 na coluna da linha anterior, ele coloca o valor na coluna da linha anterior
                if (tabuleiro[l][c] != 0):
                    if l == 1:
                        if (tabuleiro[l-1][c]) == 0:
                            tabuleiro[l-1][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                            
                        # Soma valores idênticos  
                        else:  
                            somaNumerosIdenticos(tabuleiro, l, c)
                                
                    elif l == 2:
                        if (tabuleiro[l-2][c] == 0):
                            tabuleiro[l-2][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l-1][c] == 0):
                            tabuleiro[l-1][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                            
                        # Soma valores idênticos
                        if (tabuleiro[l-1][c] == tabuleiro[l][c]):
                            somaNumerosIdenticos(tabuleiro, l, c)
                        
                    elif l == 3:
                        if (tabuleiro[l-3][c] == 0):
                            tabuleiro[l-3][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l-2][c] == 0):
                            tabuleiro[l-2][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l-1][c] == 0):
                            tabuleiro[l-1][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        
                        # Soma valores idênticos
                        if (tabuleiro[l-1][c] == tabuleiro[l][c]):
                            somaNumerosIdenticos(tabuleiro, l, c)
                            
    # Movimento para baixo                    
    elif (escolha == 2):
        for l in range (0,4):
            for c in range (0,4):
                if (tabuleiro[l][c] != 0):
                    
                    if l == 0:
                        if (tabuleiro[l+3][c] == 0):
                            tabuleiro[l+3][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l+2][c] == 0):
                            tabuleiro[l+2][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l+1][c] == 0):
                            tabuleiro[l+1][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                            
                    elif l == 1:
                        if (tabuleiro[l+2][c] == 0):
                            tabuleiro[l+2][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l+1][c] == 0):
                            tabuleiro[l+1][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                    
                    elif l == 2:
                        if (tabuleiro[l+1][c]) == 0:
                            tabuleiro[l+1][c] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
    # Movimento para esquerda            
    elif (escolha == 3):
        for l in range (0,4):
            for c in range (0,4):
                if (tabuleiro[l][c] != 0):
                    
                    if c == 1:
                        if (tabuleiro[l][c-1]) == 0:
                            tabuleiro[l][c-1] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                            
                    elif c == 2:
                        if (tabuleiro[l][c-2] == 0):
                            tabuleiro[l][c-2] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l][c-1] == 0):
                            tabuleiro[l][c-1] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        
                    elif c == 3:
                        if (tabuleiro[l][c-3] == 0):
                            tabuleiro[l][c-3] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l][c-2] == 0):
                            tabuleiro[l][c-2] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l][c-1] == 0):
                            tabuleiro[l][c-1] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
    # Movimento para direita     
    elif (escolha == 4):
        for l in range (0,4):
            for c in range (0,4):
                if (tabuleiro[l][c] != 0):

                    if c == 0:
                        if (tabuleiro[l][c+3] == 0):
                            tabuleiro[l][c+3] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l][c+2] == 0):
                            tabuleiro[l][c+2] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l][c+1] == 0):
                            tabuleiro[l][c+1] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                            
                    elif c == 1:
                        if (tabuleiro[l][c+2] == 0):
                            tabuleiro[l][c+2] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                        elif (tabuleiro[l][c+1] == 0):
                            tabuleiro[l][c+1] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
                    
                    elif c == 2:
                        if (tabuleiro[l][c+1]) == 0:
                            tabuleiro[l][c+1] = tabuleiro[l][c]
                            tabuleiro[l][c] = 0
        

def somaNumerosIdenticos (tabuleiro, l, c):
    soma = 0
    if l == 1:
        if (tabuleiro[l-1][c] == tabuleiro[l][c]):
            soma = tabuleiro[l-1][c] + tabuleiro[l][c]
            tabuleiro[l-1][c] = soma
            tabuleiro[l][c] = 0
    elif l == 2:
            soma = tabuleiro[l-1][c] + tabuleiro[l][c]
            tabuleiro[l-1][c] = soma
            tabuleiro[l][c] = 0
    elif l == 3:
            soma = tabuleiro[l-1][c] + tabuleiro [l][c]
            tabuleiro[l-1][c] = soma
            tabuleiro [l][c] = 0  
            
    
# Programa principal
tabuleiro_origem =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
opcao = 0

while (opcao != 3):
    
    opcao = menu() 
    
    if opcao == 1:
        # Recebe números aleatórios para por em posições aleatórias no tabuleiro o número 2
        l1, c1 = geraNumeros()
        l2, c2 = geraNumeros()
        tabuleiro_origem[l1][c1] = 2

        # A condição abaixo serve para anular as posições iguais, pois devem estar em posições diferentes
        if (l1 == l2 and c1 == c2):
            l2, c2 = geraNumeros()
        else:
            tabuleiro_origem[l2][c2] = 2
            
        tabuleiroOriginalZerado(tabuleiro_origem)
        
        movimentandoBlocos(tabuleiro_origem)
        
        tabuleiroOriginalZerado(tabuleiro_origem)
        
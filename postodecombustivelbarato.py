#Autor: Caroline Santos de Jesus
#Componente Curricular: Algoritmos I
#Concluído em: 03/09/2023
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
#código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

postos = [{'posto': 'Posto Ipiranga', 'Gasolina': 5.50, 'Etanol': 3.80, 'Diesel': 4.50},  
          {'posto': 'Posto Menor Valor', 'Gasolina': 5.65, 'Etanol': 3.75, 'Diesel': 4.85},
          {'posto': 'Posto Shell', 'Gasolina': 5.40, 'Etanol': 3.90, 'Diesel': 4.60}]

opcao = opcao_combustivel = litros_combustivel = qntd_consultas = qntd_MinIpi = qntd_MenorValor = qntd_MinShell = qntd_litrosIpi = qntd_litrosMenorValor = qntd_litrosShell = 0
relacaoValorMenor_Gaso = postos[0]['Gasolina']
relacaoValorMenor_Eta = postos[0]['Etanol']
relacaoValorMenor_Die = postos[0]['Diesel']
relacaoValorMaior_Gaso = postos[0]['Gasolina']
relacaoValorMaior_Eta = postos[0]['Etanol']
relacaoValorMaior_Die = postos[0]['Diesel']
relacaoGaso_nomeMenor = relacaoEta_nomeMenor = relacaoDie_nomeMenor = ''
relacaoGaso_nomeMaior = relacaoEta_nomeMaior = relacaoDie_nomeMaior = ''

resposta = 'Sim'

while (opcao != 4):
  
  print()
  print('-=-=-=-=-=-=-=-=-= MENU DE OPÇÕES -=-=-=-=-=-=-=-=-=')
  print('[ 1 ] Inserir dados de abastecimento do seu veículo;')
  print('[ 2 ] Exibir posto com menor valor;')
  print('[ 3 ] Exibir todos os postos')
  print('[ 4 ] Exit')
  print('-=-'*15)
  
  opcao = int(input('\n>>>> Escolha uma opção: '))
  
  if (opcao == 1):
  
    print('-=-'*15)
    print('\nQual combustivel deseja para abastecer seu veículo?\n')
    print('[ 1 ] Gasolina;')
    print('[ 2 ] Etanol;')
    print('[ 3 ] Diesel')
    print('-=-'*15)

    opcao_combustivel = int(input('\n>>>> Escolha uma das opções: '))
    litros_combustivel = int(input('>>>> Quantos litros deseja abastecer? '))

    if opcao_combustivel == 1:
      
      print(f'\nVocê deseja abastecer {litros_combustivel}L de GASOLINA? [Sim/ Não]')
      resposta = input('>>>> ')
      
      if (resposta == "Sim"):
        print()
        print('-=-'*24)
        print('Dados coletados com sucesso!!\nAgora escolha entre as opções [ 2 ] e [ 3 ] para seguir com a pesquisa.')
        print('-=-'*24)
        
      elif (resposta == "Nao"):
        print()
        print('-=-'*24)
        print('Selecione novamente a opção [ 1 ] no menu para inserir os dados corretos.')
        print('-=-'*24)

    elif opcao_combustivel == 2:
      
      print(f'\nVocê deseja abastecer {litros_combustivel}L de ETANOL? [Sim/ Não]')
      resposta = input('>>>> ')
      
      if (resposta == "Sim"):
        print()
        print('-=-'*24)
        print('Dados coletados com sucesso!!\nAgora escolha entre as opções [ 2 ] e [ 3 ] para seguir com a pesquisa.')
        print('-=-'*24)
        
      elif (resposta == "Nao"):
        print()
        print('-=-'*24)
        print('Selecione novamente a opção [ 1 ] no menu para inserir os dados corretos.')
        print('-=-'*24)

    elif opcao_combustivel == 3:

      print(f'\nVocê deseja abastecer {litros_combustivel}L de DIESEL? [Sim/ Não]')
      resposta = input('>>>> ')
      
      if (resposta == "Sim"):
        print()
        print('-=-'*24)
        print('Dados coletados com sucesso!!\nAgora escolha entre as opções [ 2 ] e [ 3 ] para seguir com a pesquisa.')
        print('-=-'*24)
        
      elif (resposta == "Nao"):
        print()
        print('-=-'*24)
        print('Selecione novamente a opção [ 1 ] no menu para inserir os dados corretos.\n')
        print('-=-'*24)
  
  elif (opcao == 2):
    
    qntd_consultas += 1
    
    if (opcao_combustivel == 0 and litros_combustivel == 0):
      
      print()
      print('-=-'*24)
      print('> Primeiro é necessário que você insira o tipo de combustível e quantidade\n  de litros que deseja para que a análise seja feita.')
      print('> Digite [ 1 ] no menu de opções para escolher o combustivel de sua preferência\n  e a quantidade de litros que deseja abastecer.')
      print('-=-'*24)
      
    else:  
      
      if opcao_combustivel == 1:
        
        menorValorCom = postos[0]['Gasolina']
        nomePostoMenor = postos[0]['posto']
        indice = precoBaixo = 0

        for i in range (0,3):
            if postos[i]['Gasolina'] < menorValorCom:
                menorValorCom = postos[i]['Gasolina']
                nomePostoMenor = postos[i]['posto']
                
                indice = i
        
        precoBaixo = menorValorCom * litros_combustivel
        
        print()
        print()
        print('-=-=-=-=-=-=-=-=-=-=-=-=- VALORES DOS COMBUSTÍVEIS -=-=-=-=-=-=-=-=-=-=-=-')
        print()
        print(f'Posto com MENOR VALOR a GASOLINA:')
        print(f'> Posto {nomePostoMenor} ---> R$ {round(menorValorCom, 2)}/l.')
        print(f'  > Neste posto você irá pagar no total por {litros_combustivel}l: R$ {round(precoBaixo, 2)}.')
        print()
        print('-=-=-=-=-=-=-=-=-=-=-=-=-==-=- DEMAIS POSTOS -=-=-=-=-=-=-==-=-=-=-=-=-=-=')   
        for i in range(0,3):
            if indice != i:
              precoAlto = 0
              print()
              print(f'> {postos[i]["posto"]} ---> R$ {postos[i]["Gasolina"]}')
              precoAlto = postos[i]['Gasolina'] * litros_combustivel
              print(f'  > Neste posto você irá pagar no total por {litros_combustivel}l: R$ {round(precoAlto, 2)}.')
              print(f'  > Escolhendo o posto {nomePostoMenor}, você economizaria R$ {round(precoAlto - precoBaixo, 2)}.')
        print('-=-'*24)  
        
      elif opcao_combustivel == 2:
        
        menorValorCom = postos[0]['Etanol']
        nomePostoMenor = postos[0]['posto']
        indice = 0

        for i in range (0,3):
            if postos[i]['Etanol'] < menorValorCom:
                menorValorCom = postos[i]['Etanol']
                nomePostoMenor = postos[i]['posto']
                indice = i
          
         
        precoBaixo = menorValorCom * litros_combustivel
        
        print()
        print()
        print('-=-=-=-=-=-=-=-=-=-=-=-=- VALORES DOS COMBUSTÍVEIS -=-=-=-=-=-=-=-=-=-=-=-')
        print()
        print(f'Posto com MENOR VALOR a ETANOL:')
        print(f'> Posto {nomePostoMenor} ---> R$ {round(menorValorCom, 2)}/l.')
        print(f'  > Neste posto você irá pagar no total por {litros_combustivel}l: R$ {round(precoBaixo, 2)}.')
        print()
        print('-=-=-=-=-=-=-=-=-=-=-=-=-==-=- DEMAIS POSTOS -=-=-=-=-=-=-==-=-=-=-=-=-=-=')   
        for i in range(0,3):
            if indice != i:
              precoAlto = 0
              print()
              print(f'> {postos[i]["posto"]} ---> R$ {postos[i]["Etanol"]}')
              precoAlto = postos[i]['Etanol'] * litros_combustivel
              print(f'  > Neste posto você irá pagar no total por {litros_combustivel}l: R$ {round(precoAlto, 2)}.')
              print(f'  > Escolhendo o posto {nomePostoMenor}, você economizaria R$ {round(precoAlto - precoBaixo, 2)}.')
        print('-=-'*24) 
        
      elif opcao_combustivel == 3:
        
        menorValorCom = postos[0]['Diesel']
        nomePostoMenor = postos[0]['posto']
        indice = 0

        for i in range (0,3):
            if postos[i]['Diesel'] < menorValorCom:
                menorValorCom = postos[i]['Diesel']
                nomePostoMenor = postos[i]['posto']
                indice = i

        precoBaixo = menorValorCom * litros_combustivel
        
        print()
        print()
        print('-=-=-=-=-=-=-=-=-=-=-=-=- VALORES DOS COMBUSTÍVEIS -=-=-=-=-=-=-=-=-=-=-=-')
        print()
        print(f'Posto com MENOR VALOR a DIESEL:')
        print(f'> Posto {nomePostoMenor} ---> R$ {round(menorValorCom, 2)}/l.')
        print(f'  > Neste posto você irá pagar no total por {litros_combustivel}l: R$ {round(precoBaixo, 2)}.')
        print()
        print('-=-=-=-=-=-=-=-=-=-=-=-=-==-=- DEMAIS POSTOS -=-=-=-=-=-=-==-=-=-=-=-=-=-=')   
        for i in range(0,3):
            if indice != i:
              precoAlto = 0
              print()
              print(f'> {postos[i]["posto"]} ---> R$ {postos[i]["Diesel"]}')
              precoAlto = postos[i]['Diesel'] * litros_combustivel
              print(f'  > Neste posto você irá pagar no total por {litros_combustivel}l: R$ {round(precoAlto, 2)}.')
              print(f'  > Escolhendo o posto {nomePostoMenor}, você economizaria R$ {round(precoAlto - precoBaixo, 2)}.')
        print('-=-'*24) 
        
      else: 
        print('Digite um valor válido!')
      
    if nomePostoMenor == 'Posto Ipiranga':
      qntd_MinIpi += 1 
      qntd_litrosIpi += litros_combustivel
      
    elif nomePostoMenor == 'Posto Menor Valor':
      qntd_MenorValor += 1
      qntd_litrosMenorValor += litros_combustivel 
      
    elif nomePostoMenor == 'Posto Shell':
      qntd_MinShell += 1  
      qntd_litrosShell += litros_combustivel
      
  elif (opcao == 3):
    
    qntd_consultas += 1
    
    print()
    print()
    print('-=-=-=-=-=-=-=-=- POSTOS DE COMBUSTÍVEIS -=-=-=-=-=-=-=-')
    for i in range (0,3):
      print()
      print(f'> {postos[i]["posto"]}: ')
      print(f'  > Gasolina ---> R$ {postos[i]["Gasolina"]}')
      print(f'  > Etanol ---> R$ {postos[i]["Etanol"]}')
      print(f'  > Diesel ---> R$ {postos[i]["Diesel"]}')
      print()
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    
  elif (opcao == 4):
    
    print('Programa finalizado')
    
  else:
    print('\nOpção inválida. Tente novamente.\n')

relacaoValorMenor_Gaso = postos[0]['Gasolina']
relacaoValorMenor_Eta = postos[0]['Etanol']
relacaoValorMenor_Die = postos[0]['Diesel']

relacaoValorMaior_Gaso = postos[0]['Gasolina']
relacaoValorMaior_Eta = postos[0]['Etanol']
relacaoValorMaior_Die = postos[0]['Diesel']

print()
print('-=-=-=-=-=-=-=-=-=-=-=- RELATÓRIO FINAL -=-=-=-=-=-=-=-=-=-=-=-=-') 
print()

print (f'> Quantidade de consultas realizadas no sistema: {qntd_consultas}')

print('---'*24)

print(f'> Quantidade de vezes que cada posto teve o menor valor:')
print(f'  > Posto Ipiranga: {qntd_MinIpi}')
print(f'  > Posto Menor Valor: {qntd_MenorValor}')
print(f'  > Posto Shell: {qntd_MinShell}')

print('---'*24)

print(f'> Média de litros consultados por posto:')
print(f'  > Posto Ipiranga: {qntd_litrosIpi / qntd_MinIpi}')
print(f'  > Posto Menor Valor: {qntd_litrosMenorValor / qntd_MenorValor}')
print(f'  > Posto Shell: {qntd_litrosShell / qntd_MinShell}')

print('---'*24)

print(f'> Relação, por combustível, do posto que possui o MAIOR VALOR e o MENOR VALOR:')
for i in range (0,3):
  # Menor valor
  if postos[i]['Gasolina'] < relacaoValorMenor_Gaso:
    
    relacaoValorMenor_Gaso = postos[i]['Gasolina']
    relacaoGaso_nomeMenor = postos[i]['posto']
    
  if postos[i]['Etanol'] < relacaoValorMenor_Eta:
    
    relacaoValorMenor_Eta = postos[i]['Etanol']
    relacaoEta_nomeMenor = postos[i]['posto']
    
  if postos[i]['Diesel'] < relacaoValorMenor_Die:
    
    relacaoValorMenor_Die = postos[i]['Diesel']
    relacaoDie_nomeMenor = postos[i]['posto']
  
  # Maior valor
  if postos[i]['Gasolina'] > relacaoValorMaior_Gaso:
    
    relacaoValorMaior_Gaso = postos[i]['Gasolina']
    relacaoGaso_nomeMaior = postos[i]['posto']
  
  if postos[i]['Etanol'] > relacaoValorMaior_Eta:
    
    relacaoValorMaior_Eta = postos[i]['Etanol']
    relacaoEta_nomeMaior = postos[i]['posto']
    
  if postos[i]['Diesel'] > relacaoValorMaior_Die:

    relacaoValorMaior_Die = postos[i]['Diesel']
    relacaoDie_nomeMaior = postos[i]['posto']
    
print(f'  > Posto com MENOR VALOR a GASOLINA---> {relacaoGaso_nomeMenor}: R$ {relacaoValorMenor_Gaso}')
print(f'  > Posto com MENOR VALOR a ETANOL---> {relacaoEta_nomeMenor}: R$ {relacaoValorMenor_Eta}')
print(f'  > Posto com MENOR VALOR a DIESEL---> {relacaoDie_nomeMenor}: R$ {relacaoValorMenor_Die}')

print(f'  > Posto com MAIOR VALOR a GASOLINA---> {relacaoGaso_nomeMaior}: R$ {relacaoValorMaior_Gaso}')
print(f'  > Posto com MAIOR VALOR a ETANOL---> {relacaoEta_nomeMaior}: R$ {relacaoValorMaior_Eta}')
print(f'  > Posto com MAIOR VALOR a DIESEL---> {relacaoDie_nomeMaior}: R$ {relacaoValorMaior_Die}')

print()
print('---'*24)

#Autor: Caroline Santos de Jesus
#Componente Curricular: Algoritmos I
#Concluído em: 25/09/2022
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
#código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

#Dicionário criado para armazenar as áreas totais por estado.
total_estados={"BA": 0, "PE": 0, "CE": 0, "MA": 0, "AL": 0, "RN": 0, "PB": 0, "PI": 0, "SE": 0}

#Dicionário criado para armazenar as áreas totais por cada tipo de árvore.
total_arvores={"Cajueiro": 0 , "Mangueira": 0, "Dende": 0, "Coqueiro": 0, "Bambu gigante": 0, "Ipe": 0}

area=soma_regiao=qntd_cajueiro=qntd_mangueira=qntd_dende=qntd_coqueiro=qntd_bambu=qntd_ipe=area_ba=area_pe=area_ce=area_ma=area_al=area_rn=area_pb=area_pi=area_se=0
menor_ba=menor_pe=menor_ce=menor_ma=menor_al=menor_rn=menor_pb=menor_pi=menor_se=maior_extensao=nome_maior_arvore=maximo_arvores=nome_menor_arvore=0
minimo_arvores=codigo_maior_extensao=cidade_maior_extensao=estado_maior_extensao=arvore_maior_extensao=menor_nome_extensao=menor_extensao=0

#Variável reposta começa com True para indicar que a expressão a ser executada é verdadeira.
resposta=True
print("===============================================================")
print("          SISTEMA DE GERENCIAMENTO DE REFLORESTAMENTO          ")
print("===============================================================")
while resposta:
    print ("1) Adicionar dados")
    print ("2) Exibir relatório")
    print ("0) Sair")
    resposta=int(input("Digite a opção desejada: "))
    if resposta == 0:
        break 
    elif resposta == 1:
        codigo_area=input("DIGITE O CÓDIGO DA ÁREA: ")
        print("---------------------------------------------------------------")
        cidade=input("DIGITE A SIGLA DA CIDADE: ").upper()
        print("---------------------------------------------------------------")
        print("Bahia -> BA")
        print("Pernambuco -> PE")
        print("Ceará -> CE")
        print("Maranhão -> MA")
        print("Alagoas -> AL")
        print("Rio Grande do Norte -> RN")
        print("Paraíba -> PB")
        print("Piauí -> PI")
        print("Sergipe -> SE")
        estado=input("DIGITE A SIGLA DO ESTADO: ").upper()
        print("---------------------------------------------------------------")
        print("DIGITE A DIMENSÃO DA ÁREA REFLORESTADA:")
        altura=float(input("Altura: "))
        base=float(input("Base: "))
        print("---------------------------------------------------------------")
        print("TIPO DE ÁRVORE:")
        print("Cajueiro")
        print("Mangueira")
        print("Dende")
        print("Coqueiro")
        print("Bambu gigante")
        print("Ipe")
        tipo_arvore=input("ESCOLHA UMA DAS OPÇÕES ACIMA DE ACORDO COM O\nTIPO DE ÁRVORE USADO NO REFLORESTAMENTO: ").capitalize()
        print("---------------------------------------------------------------")
        
        area=altura*base
        
        #Adicionando a dimensão das áreas no dicionário referente aos estados digitados pelo usuário.
        if estado in total_estados: 
            total_estados[estado] += area
            
        soma_regiao+=area 
    
        #Adicionando ao dicionário a área reflorestada por cada tipo de árvore digitada pelo usuário.
        if tipo_arvore in total_arvores: 
            total_arvores[tipo_arvore]+=area
    
        if tipo_arvore == "Cajueiro":
            qntd_cajueiro+=1
        elif tipo_arvore == "Mangueira":
            qntd_mangueira+=1
        elif tipo_arvore == "Dende":
            qntd_dende+=1
        elif tipo_arvore == "Coqueiro":
            qntd_coqueiro+=1
        elif tipo_arvore == "Bambu gigante":
            qntd_bambu+=1
        elif tipo_arvore == "Ipe":
            qntd_ipe+=1
            
        #Pegando o menor e maior número de árvores usadas.
        maximo_arvores=max(qntd_cajueiro,qntd_mangueira,qntd_dende,qntd_coqueiro,qntd_bambu,qntd_ipe)  
        minimo_arvores=min(qntd_cajueiro,qntd_mangueira,qntd_dende,qntd_coqueiro,qntd_bambu,qntd_ipe)
        
        #Armazenando o nome da maior árvore utilizada em uma variável.
        if maximo_arvores == qntd_cajueiro:
            nome_maior_arvore = "Cajueiro"
        elif maximo_arvores == qntd_mangueira:
            nome_maior_arvore = "Mangueira"
        elif maximo_arvores == qntd_dende:
            nome_maior_arvore = "Dende"
        elif maximo_arvores == qntd_coqueiro:
            nome_maior_arvore = "Coqueiro"
        elif maximo_arvores == qntd_bambu:
            nome_maior_arvore = "Bambu gigante"
        elif maximo_arvores == qntd_ipe:
            nome_maior_arvore = "Ipe"   
            
        #Armazenando o nome da menor árvore utilizada em uma variável.
        if minimo_arvores == qntd_cajueiro:
            nome_menor_arvore = "Cajueiro"
        elif minimo_arvores == qntd_mangueira:
            nome_menor_arvore = "Mangueira"
        elif minimo_arvores == qntd_dende:
            nome_menor_arvore = "Dende"
        elif minimo_arvores == qntd_coqueiro:
            nome_menor_arvore = "Coqueiro"
        elif minimo_arvores == qntd_bambu:
            nome_menor_arvore = "Bambu gigante"
        elif minimo_arvores == qntd_ipe:
            nome_menor_arvore = "Ipe"
        
        #Pegando os dados da maior extensão da área reflorestada. 
        if area > maior_extensao:
            maior_extensao = area
            codigo_maior_extensao = codigo_area
            cidade_maior_extensao = cidade
            estado_maior_extensao = estado
            arvore_maior_extensao = tipo_arvore
        
        #Adicionando mais 1 as áreas reflorestadas por estado e adicionando as áreas em variáveis referentes ao estado ditado pelo usuário.
        if estado == "BA":
            area_ba+=1
            menor_ba+=area
        elif estado == "PE":
            area_pe+=1
            menor_pe+=area
        elif estado == "CE":
            area_ce+=1
            menor_ce+=area
        elif estado == "MA":
            area_ma+=1
            menor_ma+=area
        elif estado == "AL":
            area_al+=1
            menor_al+=area
        elif estado == "RN":
            area_rn+=1
            menor_rn+=area
        elif estado == "PB":
            area_pb+=1
            menor_pb+=area
        elif estado == "PI":
            area_pi+=1
            menor_pi+=area
        elif estado == "SE":
            area_se+=1
            menor_se+=area
        
        #Pegando a área menos reflorestada.
        menor_extensao=min(menor_ba,menor_pe,menor_ce,menor_ma,menor_al,menor_rn,menor_pb,menor_pi,menor_se)
        
        #Associando área menos reflorestada ao seu estado.
        if menor_extensao == menor_ba:
            menor_nome_extensao = "Bahia"
        elif menor_extensao == menor_pe:
            menor_nome_extensao = "Pernambuco"
        elif menor_extensao == menor_ce:
            menor_nome_extensao = "Ceará"
        elif menor_extensao == menor_ma:
            menor_nome_extensao = "Maranhão"
        elif menor_extensao == menor_al:
            menor_nome_extensao = "Alagoas"
        elif menor_extensao == menor_rn:
            menor_nome_extensao = "Rio Grande do Sul"
        elif menor_extensao == menor_pb:
            menor_nome_extensao = "Paraíba"
        elif menor_extensao == menor_pi:
            menor_nome_extensao = "Piauí"
        elif menor_extensao == menor_se:
            menor_nome_extensao = "Sergipe"
    
    elif resposta == 2:
        print("===============================================================")
        print("                           RELATÓRIO                           ")
        print("===============================================================")
        print("Área total reflorestada por estado:")
        print(f"{total_estados}, em km²")
        print("---------------------------------------------------------------")
        print("Área total geral reflorestada da Região Nordeste: ", soma_regiao, "km²")
        print("---------------------------------------------------------------")
        print("Área total reflorestada por cada tipo de árvore:")
        print(f"{total_arvores}, em km²")
        print("---------------------------------------------------------------")
        print(f"Árvore mais usada: {nome_maior_arvore} = {maximo_arvores}")
        print(f"Árvore menos usada: {nome_menor_arvore} = {minimo_arvores}")
        print("---------------------------------------------------------------")
        print("Dados da maior extensão da área reflorestada:")
        print(f"Código = {codigo_maior_extensao}")
        print(f"Cidade = {cidade_maior_extensao}")
        print(f"Estado = {estado_maior_extensao}")
        print(f"Tipo de árvore = {arvore_maior_extensao}")
        print(f"Área = {maior_extensao} km²")
        print("---------------------------------------------------------------")
        print("Quantidade de áreas reflorestadas por estado:")
        print(f"Bahia = {area_ba}")
        print(f"Pernambuco = {area_pe}")
        print(f"Ceará = {area_ce}")
        print(f"Maranhão = {area_ma}")
        print(f"Alagoas= {area_al}")
        print(f"Rio Grande do Sul= {area_rn}")
        print(f"Paraíba= {area_pb}")
        print(f"Piauí = {area_pi}")
        print(f"Sergipe = {area_se}")
        print("---------------------------------------------------------------")   
        print("Estado MENOS reflorestado para ações futuras:")
        print(f"{menor_nome_extensao} = {menor_extensao} km²")
        print("===============================================================")
# Projeto insperado do canal do YouTube HASHTAG PROGRAMAÇÃO - Análise de vendas de uma determinada empresa

# Passo a passo de solução
# Lógica de programação

# Passo 1 - Percorrer todos os arquivos da pasta de dados (PASTA VENDAS)
# Passo 2 - Importar as bases de dados de vendas
# Passo 3 - Tratar / Compilar as bases de dados
# Passo 4 - Calcular o produto mais vendido (em quantidade)
# Passo 5 - Calcular o produto que mais faturou
# Passo 6 - Calcular a loja / cidade que mais vendeu (em faturamento)
# Passo 7 - Criar gráfico / dashboard em relação ao faturamento de cada cidade

import pandas as pd 
import os 
import plotly.express as px

def titulo (): #Função criada apenas para deixar o código um pouco mais organizado
    print("{} Análise de Vendas {}".format('=='*6, '=='*6))
    print(" -- "*11)
   
    
def titulo2 ():
    print(" -- "*11)
       
    
# Diretório onde os arquivos Excel estão localizados
diretorio = "C:\\Users\\Caroline\\Documents\\Curso de Python\\Vendas"

tabela_total = pd.DataFrame()

# Percorrer todos os arquivos da pasta de dados (pasta vendas), importar as bases de dados de vendas e tratar / compilar as bases de dados
for arquivo in os.listdir(diretorio):
    if "Vendas - Belo Horizonte" in arquivo or "Vendas - Curitiba" in arquivo or "Vendas - Fortaleza" in arquivo or "Vendas - Goiás" in arquivo or "Vendas - Porto Alegre" in arquivo or "Vendas - Recife" in arquivo or "Vendas - Rio de Janeiro" in arquivo or "Vendas - Salvador" in arquivo or "Vendas - São Paulo" in arquivo: 
        caminho_arquivo = diretorio + "\\" + arquivo
        tabela = pd.read_csv(caminho_arquivo)
        tabela_total = pd.concat([tabela_total, tabela])

titulo()

# Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print("Quantidade vendida de cada produto:\n")
print(tabela_produtos)

# Calcular o produto que mais faturou
tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"]  * tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
titulo2()
print("Faturamento obtido por cada produto:\n")
print(tabela_faturamento)

# Calcular a loja/ cidade que mais vendeu (em faturamento)
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
titulo2()
print("Faturamento obtido nas lojas de cada cidade:\n")
print(tabela_lojas)

# Criar gráfico / dashboard em relação ao faturamento de cada cidade
grafico = px.bar(tabela_lojas, x = tabela_lojas.index, y = 'Faturamento')
grafico.show()


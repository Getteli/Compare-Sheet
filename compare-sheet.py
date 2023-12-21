import pandas as pd

# Carregue os arquivos CSV em dois DataFrames
df1 = pd.read_csv('tabela1.csv')
df2 = pd.read_csv('tabela2.csv')

# Compare os DataFrames e encontre as diferenças
# diferencas = pd.concat([df1, df2]).drop_duplicates(keep=False)
# diferencas = df1.compare(df2)
diferencas = df1[df1 != df2].stack()

# Se houver diferenças, exiba as linhas correspondentes
if not diferencas.empty:
    # print("Valores que não batem:")
    # print(diferencas)
    print("Diferenças nas colunas:")
    for (linha, coluna), valor in diferencas.items():
        # linha com +2 por conta do titulo na 1° e por que começa com 0
        print(f"Linha: numero {linha+2}\n")
        # lista todas as colunas da linha diferente
        print(f"Colunas: {coluna} \n")
        # exibe os dados da tabela 1 e 2 para ver a diferença
        print("Tabela 1:\n")
        print(f"{df1.at[linha, coluna]} \n")
        print("Tabela 2:\n")
        print(f"{df2.at[linha, coluna]} \n")
else:
    print("As tabelas são iguais.")

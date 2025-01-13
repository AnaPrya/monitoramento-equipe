import openpyxl
import pandas as pd  # Para manipular os dados como DataFrame

# Caminho do arquivo .xlsm
excel_path = r'C:\Users\abartolo\Desktop\Monitoramento.xlsm'

# Abrindo o arquivo
wb = openpyxl.load_workbook(excel_path, keep_vba=True)

# Selecionando uma planilha específica
sheet = wb['Tabela Base']  # Substitua 'NomeDaAba' pelo nome da aba desejada

# Definindo o intervalo de células (A1:J53)
tabela = sheet['A1:J53']

# Inicializando uma lista para armazenar os dados
dados = []

# Iterando sobre as linhas e colunas do intervalo
for linha in tabela:
    dados_linha = [celula.value for celula in linha]  # Coleta os valores de cada célula na linha
    dados.append(dados_linha)

# Transformando os dados em DataFrame para facilitar a manipulação
df = pd.DataFrame(dados)

# Exibindo os primeiros dados
print(df.head())

#_____________________________________________________

import pandas as pd
from sqlalchemy import create_engine

# Carregar os dados da planilha Excel
excel_path = "C:/Users/abartolo/Desktop/Monitoramento.xlsm"
df = pd.read_excel(excel_path, sheet_name="Tabela_Base", usecols="A:J", skiprows=0, nrows=53, header=0)

# Criar uma conexão com o banco de dados SQL (usando SQLite como exemplo)
engine = create_engine('sqlite:///monitoramento.db')  # Cria um arquivo de banco de dados SQLite

# Carregar os dados para o banco de dados
df.to_sql('monitoramento_atividades', con=engine, if_exists='replace', index=False)

print("Dados carregados para o SQL com sucesso!")
#____________________________________________________

import pandas as pd
from sqlalchemy import create_engine

# Criar a conexão com o banco de dados SQLite
engine = create_engine('sqlite:///monitoramento.db')

# Carregar os dados da tabela 'monitoramento_atividades' do banco de dados
df = pd.read_sql('SELECT * FROM monitoramento_atividades', con=engine)

# Exibir os dados
print(df)

#___________________________________________________

import pandas as pd
from sqlalchemy import create_engine

# Carregar os dados da planilha Excel
excel_path = "C:/Users/abartolo/Desktop/Monitoramento.xlsm"
df = pd.read_excel(excel_path, sheet_name="Planilha1", usecols="A:J", header=0)

# Criar uma conexão com o banco de dados SQL (usando SQLite como exemplo)
engine = create_engine('sqlite:///monitoramento.db')  # Cria um arquivo de banco de dados SQLite

# Carregar os dados para o banco de dados
df.to_sql('monitoramento_atividades', con=engine, if_exists='replace', index=False)

print("Dados carregados para o SQL com sucesso!")

#_________________________________________________



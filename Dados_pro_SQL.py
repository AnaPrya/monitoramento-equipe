import openpyxl
import pandas as pd  # Para manipular os dados como DataFrame

# Caminho do arquivo .xlsm
excel_path = 'C:/Users/abartolo/JGP Gestão de Recursos/ESG Team - General/ABartolo/Outros/Monitoramento Atividades Time.xlsm'

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
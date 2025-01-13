import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Conectar ao banco de dados SQLite
engine = create_engine('sqlite:///monitoramento.db')

# Buscar os dados da tabela no SQL
df = pd.read_sql('SELECT * FROM monitoramento_atividades', con=engine)

# Exibir dados da tabela na interface
st.title('Monitoramento de Atividades da Equipe')
st.write("Aqui estão os dados atuais. Preencha as células que precisam ser atualizadas:")

# Mostrar a tabela de dados
st.dataframe(df)

# Adicionar campos para editar os dados
# Para simplificar, estamos criando um campo de entrada para cada coluna da tabela
for index, row in df.iterrows():
    st.write(f"Editar dados da linha {index + 1}:")
    for col in df.columns:
        # Cria campos para editar as células
        novo_dado = st.text_input(f'{col} (linha {index + 1})', value=row[col])
        
        # Atualizar o dado na tabela
        df.at[index, col] = novo_dado

# Botão para salvar os dados no banco SQL
if st.button('Salvar alterações'):
    # Salvar os dados atualizados no banco SQL
    df.to_sql('monitoramento_atividades', con=engine, if_exists='replace', index=False)
    st.success('Dados salvos com sucesso!')

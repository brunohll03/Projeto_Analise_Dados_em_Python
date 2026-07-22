# Módulo responsável pela análise exploratória dos dados.
# Neste arquivo são implementadas funções para analisar,
# resumir e extrair informações relevantes dos dados.


def analisar_dados(df):                                # Função responsável pela análise dos dados

    print("Quantidade de registros:")                   # Exibe o título da quantidade de registros

    print(len(df))                                      # Exibe a quantidade total de registros


    print("\nDimensões do DataFrame:")                  # Exibe o título das dimensões do DataFrame

    print(df.shape)                                     # Exibe a quantidade de linhas e colunas


    print("\nColunas disponíveis:")                     # Exibe o título das colunas disponíveis

    print(df.columns)                                   # Exibe os nomes das colunas do DataFrame


    print("\nTipos de dados:")                          # Exibe o título dos tipos de dados

    print(df.dtypes)                                    # Exibe o tipo de dado de cada coluna


    print("\nResumo estatístico:")                      # Exibe o título do resumo estatístico

    print(df.describe())                               # Exibe estatísticas descritivas das colunas numéricas


    return df                                           # Retorna o DataFrame analisado
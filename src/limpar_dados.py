# Módulo responsável pela limpeza e preparação dos dados.
# Neste arquivo são implementadas funções para tratar dados ausentes,
# remover duplicidades, corrigir inconsistências e preparar os dados
# para as etapas de análise.


import pandas as pd                                      # Importa a biblioteca Pandas para manipulação dos dados


def limpar_dados(df):                                    # Função responsável pela limpeza e preparação dos dados

    df["nome"] = df["nome"].str.strip()                  # Remove espaços no início e no final dos nomes

    df["cidade"] = df["cidade"].str.strip().str.lower()  # Remove espaços e padroniza cidades para letras minúsculas

    df["especialidade"] = df["especialidade"].str.strip().str.lower() # Remove espaços e padroniza especialidades para letras minúsculas

    df["status"] = df["status"].str.strip().str.lower() # Remove espaços e padroniza status para letras minúsculas

    df["email"] = df["email"].str.strip().str.lower()   # Remove espaços e padroniza e-mails para letras minúsculas

    df = df.drop_duplicates()                            # Remove registros completamente duplicados

    df = df.drop_duplicates(subset="email")              # Remove registros duplicados com base no e-mail

    df.loc[(df["idade"] < 0) | (df["idade"] > 100), "idade"] = pd.NA  # Substitui idades inválidas por valores ausentes

    df["idade"] = df["idade"].fillna(df["idade"].median())             # Preenche valores ausentes com a mediana das idades válidas

    return df                                             # Retorna o DataFrame após a limpeza
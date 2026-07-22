# Módulo responsável pela análise dos dados.
# Neste arquivo serão implementadas funções para realizar cálculos,
# agrupamentos, estatísticas e identificar informações relevantes
# a partir dos dados tratados.


def analisar_dados(df):
    quantidade_atendimentos = len(df)

    idade_media = df["idade"].mean()

    atendimentos_por_especialidade = df["especialidade"].value_counts()

    return (quantidade_atendimentos, idade_media, atendimentos_por_especialidade)

# Arquivo principal responsável por executar o fluxo de processamento dos dados.
# Neste arquivo as funções de carregamento, limpeza e análise são organizadas
# para executar o pipeline completo do projeto.


from src.carregar_dados import carregar_dados        # Importa a função responsável por carregar os dados

from src.limpar_dados import limpar_dados            # Importa a função responsável pela limpeza dos dados


df = carregar_dados()                                # Carrega os dados do arquivo CSV para um DataFrame


print("Dados antes da limpeza:")                      # Exibe o título dos dados antes da limpeza

print(df)                                            # Exibe o DataFrame original


df = limpar_dados(df)                                # Executa o processo de limpeza dos dados


print("\nDados depois da limpeza:")                   # Exibe o título dos dados depois da limpeza

print(df)                                            # Exibe o DataFrame após a limpeza
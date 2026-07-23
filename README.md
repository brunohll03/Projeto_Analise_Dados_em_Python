# Projeto de Análise de Dados

Projeto desenvolvido para aprendizado de manipulação e análise de dados utilizando Python e Pandas.

## Objetivo

O objetivo deste projeto é analisar dados fictícios de atendimentos médicos, aplicando conceitos de:

* Python
* Pandas
* NumPy
* Manipulação de dados
* Limpeza de dados
* Análise exploratória
* Visualização de dados

## Tecnologias utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

## Estrutura do projeto

```text
projeto_analise_dados/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── __init__.py
│   ├── carregar_dados.py
│   ├── limpar_dados.py
│   └── analisar_dados.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalação

```
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
.\venv\Scripts\Activate.ps1

# Instalar as dependências
pip install -r requirements.txt
```

## Execução

Com o ambiente virtual ativado:

```
python main.py
```

## Fluxo do Projeto

```text
Arquivo CSV bruto
       |
       v
Carregamento dos dados
       |
       v
Limpeza e tratamento
       |
       v
Padronização dos dados
       |
       v
Análise exploratória (EDA)
       |
       v
Geração de informações
       |
       v
Arquivo CSV tratado
```

### Técnicamente 

```text
CSV (Raw)
   |
   v
carregar_dados()
   |
   v
DataFrame
   |
   v
limpar_dados()
   |
   v
DataFrame Limpo
   |
   v
analisar_dados()
   |
   v
Análise Exploratória (EDA)
   |
   v
CSV (Processed)
```

## Comandos e Métodos do Pandas

| Comando / Método | O que faz | Status |
|---|---|---|
| `import pandas as pd` | Importa a biblioteca Pandas | Estudado |
| `pd.read_csv()` | Lê um arquivo CSV e cria um DataFrame | Estudado |
| `df` | Exibe o DataFrame | Estudado |
| `df.shape` | Mostra a quantidade de linhas e colunas | Estudado |
| `df.info()` | Mostra informações sobre colunas, tipos de dados e valores não nulos | Estudado |
| `df.describe()` | Gera estatísticas descritivas das colunas numéricas | Estudado |
| `df.isnull()` | Identifica valores ausentes | Estudado |
| `df.isnull().sum()` | Conta os valores ausentes de cada coluna | Estudado |
| `df["coluna"]` | Acessa uma coluna específica | Estudado |
| `df["coluna"].unique()` | Mostra os valores únicos de uma coluna | Estudado |
| `df["coluna"].value_counts()` | Conta a frequência de cada valor | Estudado |
| `df["coluna"].value_counts().idxmax()` | Retorna o valor mais frequente | Estudado |
| `df["coluna"].value_counts().max()` | Retorna a maior frequência encontrada | Estudado |
| `len(df)` | Retorna a quantidade de linhas do DataFrame | Estudado |
| `df["coluna"].mean()` | Calcula a média | Estudado |
| `df["coluna"].median()` | Calcula a mediana | Estudado |
| `df["coluna"].min()` | Retorna o menor valor | Estudado |
| `df["coluna"].max()` | Retorna o maior valor | Estudado |
| `df["coluna"].sum()` | Soma os valores | Estudado |
| `df["coluna"].std()` | Calcula o desvio padrão | Estudado |
| `df["coluna"].var()` | Calcula a variância | Estudado |
| `df["coluna"].count()` | Conta os valores não nulos | Estudado |
| `df["coluna"].nunique()` | Conta quantos valores únicos existem | Estudado |
| `df["coluna"].first()` | Retorna o primeiro valor | Estudado |
| `df["coluna"].last()` | Retorna o último valor | Estudado |
| `df["coluna"].prod()` | Multiplica todos os valores | Estudado |
| `df["coluna"].sem()` | Calcula o erro padrão da média | Estudado |
| `df["coluna"].quantile()` | Calcula um quantil | Estudado |
| `df["coluna"].agg()` | Aplica uma ou várias funções de agregação | Estudado |
| `df.groupby()` | Agrupa os dados por uma ou mais colunas | Estudado |
| `df.groupby().size()` | Conta a quantidade de registros em cada grupo | Estudado |
| `df.groupby().count()` | Conta valores não nulos em cada grupo | Estudado |
| `df.groupby().mean()` | Calcula a média de cada grupo | Estudado |
| `df.groupby().agg()` | Aplica várias funções de agregação em cada grupo | Estudado |
| `df.groupby(["coluna1", "coluna2"])` | Agrupa os dados usando duas ou mais colunas | Estudado |
| `.unstack()` | Transforma níveis de um índice em colunas | Estudado |
| `.unstack(fill_value=0)` | Transforma níveis do índice em colunas e substitui valores ausentes por zero | Estudado |
| `df.sort_values()` | Ordena os registros por uma coluna | Estudado |
| `df.sort_values(ascending=False)` | Ordena os registros em ordem decrescente | Estudado |
| `df.sort_values(["coluna1", "coluna2"])` | Ordena usando várias colunas | Estudado |
| `df[df["coluna"] > valor]` | Filtra registros com base em uma condição | Estudado |
| `df[df["coluna"] == valor]` | Filtra registros que possuem um valor específico | Estudado |
| `&` | Representa uma condição E | Estudado |
| `\|` | Representa uma condição OU | Estudado |
| `df.loc[]` | Permite selecionar e filtrar linhas e colunas | Estudado |
| `df.loc[condição]` | Filtra linhas usando uma condição | Estudado |
| `df.loc[condição, ["coluna1", "coluna2"]]` | Filtra linhas e seleciona colunas específicas | Estudado |
| `df.loc[condição, "coluna"] = valor` | Altera valores de uma coluna quando uma condição é atendida | Estudado |
| `df["coluna"].duplicated()` | Identifica valores duplicados | Estudado |
| `df["coluna"].duplicated(keep=False)` | Identifica todos os registros que possuem valores duplicados | Estudado |
| `df.drop_duplicates()` | Remove registros duplicados | Estudado |
| `df.drop_duplicates(subset="coluna")` | Remove duplicados considerando uma coluna específica | Estudado |
| `df.drop_duplicates(subset="coluna", keep="first")` | Remove duplicados mantendo o primeiro registro | Estudado |
| `.str.strip()` | Remove espaços no início e no final de textos | Estudado |
| `.str.lower()` | Converte textos para letras minúsculas | Estudado |
| `.fillna()` | Preenche valores ausentes | Estudado |
| `pd.NA` | Representa um valor ausente | Estudado |
| `df["coluna"].quantile(0.25)` | Calcula o primeiro quartil | Estudado |
| `df["coluna"].quantile(0.50)` | Calcula o segundo quartil ou mediana | Estudado |
| `df["coluna"].quantile(0.75)` | Calcula o terceiro quartil | Estudado |
| `df.head()` | Exibe as primeiras linhas do DataFrame | Próximo |
| `df.tail()` | Exibe as últimas linhas do DataFrame | Próximo |
| `df.sample()` | Exibe registros aleatórios do DataFrame | Próximo |
| `df.copy()` | Cria uma cópia independente do DataFrame | Próximo |
| `df.rename()` | Renomeia colunas ou índices | Próximo |
| `df.reset_index()` | Reseta o índice do DataFrame | Próximo |
| `df.set_index()` | Define uma coluna como índice | Próximo |
| `df.sort_index()` | Ordena o DataFrame pelo índice | Próximo |
| `df["coluna"].isin()` | Verifica se os valores pertencem a uma lista de valores | Próximo |
| `df["coluna"].between()` | Filtra valores dentro de um intervalo | Próximo |
| `df["coluna"].str.contains()` | Verifica se um texto contém determinado padrão | Próximo |
| `df["coluna"].str.replace()` | Substitui partes de textos | Próximo |
| `df["coluna"].str.upper()` | Converte textos para letras maiúsculas | Próximo |
| `df["coluna"].str.title()` | Converte textos para formato de título | Próximo |
| `df["coluna"].astype()` | Converte o tipo de dados de uma coluna | Próximo |
| `pd.to_numeric()` | Converte valores para formato numérico | Próximo |
| `pd.to_datetime()` | Converte valores para formato de data e hora | Próximo |
| `df["data"].dt.year` | Extrai o ano de uma coluna de data | Próximo |
| `df["data"].dt.month` | Extrai o mês de uma coluna de data | Próximo |
| `df["data"].dt.day` | Extrai o dia de uma coluna de data | Próximo |
| `df["coluna"].apply()` | Aplica uma função aos valores de uma coluna | Próximo |
| `df.apply()` | Aplica uma função a linhas ou colunas do DataFrame | Próximo |
| `df.map()` | Aplica uma função elemento por elemento em uma Series | Próximo |
| `df.replace()` | Substitui valores específicos | Próximo |
| `df.drop()` | Remove linhas ou colunas | Próximo |
| `df.dropna()` | Remove registros que possuem valores ausentes | Próximo |
| `df.fillna()` | Preenche valores ausentes | Estudado |
| `pd.concat()` | Concatena DataFrames ou Series | Próximo |
| `pd.merge()` | Combina DataFrames usando colunas relacionadas | Próximo |
| `df.pivot_table()` | Cria tabelas dinâmicas para análise | Próximo |
| `pd.crosstab()` | Cria tabelas de frequência cruzando variáveis | Próximo |
| `df.corr()` | Calcula a correlação entre colunas numéricas | Próximo |
| `df.memory_usage()` | Mostra o uso de memória do DataFrame | Próximo |
| `df.dtypes` | Mostra o tipo de dados de cada coluna | Próximo |
| `df.columns` | Mostra os nomes das colunas | Próximo |
| `df.index` | Mostra o índice do DataFrame | Próximo |

## Funções Python Utilizadas

| Comando | O que faz | Status |
|---|---|---|
| `print()` | Exibe informações no console | Estudado |
| `len()` | Retorna a quantidade de elementos | Estudado |
| `def` | Cria uma função personalizada | Estudado |
| `lambda` | Cria uma função simples e anônima | Estudado |
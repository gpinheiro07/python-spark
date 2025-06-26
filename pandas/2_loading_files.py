"""
CSV -> arquivo simples, legível e popular, porém pesado se for muito extenso

Parquet -> formato colunar e binário, tem boa performance para grandes volumes
    de dados ()

xlsx -> padrão de planilhas, formato atualizado do xls, menos performático
    que CSV e Parquet para dados grandes
"""


import pandas as pd


def load_dataframe_from_csv():
    # Carrega arquivo local
    coffee_df = pd.read_csv('pandas/coffee.csv')

    # Carrega arquivo por link
    # coffee_file = pd.read_csv(
    #     'https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial'
    #     '/refs/heads/master/warmup-data/coffee.csv'
    # )
    print(coffee_df.head())


# Precisa da lib complementar pyarrow
def load_dataframe_from_parquet():
    results_df = pd.read_parquet('pandas/results.parquet')
    print(results_df.head())


# Precisa da lib complementar openpyxl
# bem mais lento comparado ao parquet
def load_dataframe_from_excel():
    # olympics_df = pd.read_excel('pandas/olympics-data.xlsx')

    # Define qual aba da planilha vai ser carregada
    # sheet_name = 0 -> apenas a primeira aba (padrão)
    # sheet_name = None -> todas as abas, cria um dict onde cada aba é uma
    #   chave e cada valor um dataframe
    olympics_df = pd.read_excel(
        'pandas/olympics-data.xlsx',
        sheet_name="results"
    )
    print(olympics_df.head())


# load_dataframe_from_csv()
# load_dataframe_from_parquet()
load_dataframe_from_excel()

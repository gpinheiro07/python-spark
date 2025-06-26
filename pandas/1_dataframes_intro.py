"""
Pandas é uma biblioteca que nos permite manipular dados tabulares

Dataframes -> Principal estrutura da biblioteca pandas (tabelas com
    funcionalidades extras)

"""


import pandas as pd


def dataframe_basic_uses():
    # Cria um dataframe
    df = pd.DataFrame(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        columns=["A", "B", "C"],
        index=["x", "y", "z"]
    )

    print(df)

    # print(df.head()) -> acessa os primeiros valores do dataframe
    # print(df.head(1))

    # print(df.tail()) -> acessa os ultimos valores do dataframe
    # print(df.tail(1))

    # print(df.columns) -> attr: acessa as colunas do dataframe

    # print(df.index) -> attr: acessa o index do dataframe
    # print(df.index.to_list())

    # df.info() -> exibe as informações do dataframe

    # print(df.describe()) -> retorna um resumo estatítico das colunas

    # print(df.nunique()) -> retorna a quantidade de valores únicos por coluna
    # print(df["A"].unique())

    # print(df.shape) -> attr: tupla com o numero de index e colunas do df

    # print(df.size) -> attr: numero total de itens do dataframe


dataframe_basic_uses()

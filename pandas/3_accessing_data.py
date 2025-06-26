import pandas as pd


# Acessa colunas e linhas especificas do dataframe
def get_specific_data_with_loc_iloc():
    # .loc[#Rows, #Columns] -> #index, #coluna
    coffee_df = pd.read_csv('pandas/coffee.csv')
    print(coffee_df.loc[0])
    # print(coffee_df.loc[[0, 1, 5]]) -> indexes especificos
    # print(coffee_df.loc[0:3]) -> list slice
    # print(coffee_df.loc[5:8, ["Day", "Units Sold"]]) -> indexes e colunas
    #   especificas
    # print(coffee_df.loc[:, ["Day", "Units Sold"]]) -> colunas especificas

    # tranformos os indexes númericos para os dias da semana
    #   correspondentes na coluna "Day"
    # coffee_df.index = coffee["Day"]
    # coffee_df.loc["Monday":"Wednesday"]

    # Só funciona passando o valor númerico do index
    # print(coffee_df.iloc[0])


# Muda algum valor especifico dentro do df
def change_dataframe_data():
    coffee_df = pd.read_csv('pandas/coffee.csv')
    print(coffee_df.head())
    coffee_df.loc[1, "Units Sold"] = 10
    print(coffee_df.head())
    # coffee_df.loc[1:3, "Units Sold"] = 10


# Só funciona para obter valores especificos (1 index e/ou 1 coluna)
# mais otimizado que loc/iloc para valor singular
def get_specific_data_with_at_iat():
    coffee_df = pd.read_csv('pandas/coffee.csv')
    print(coffee_df.at[0, "Units Sold"])

    # Só funciona passando o valor númerico do index
    print(coffee_df.iat[0, 0])


# Não é possivel se a palavra tives espaço ex: "Units Sold"
def access_data_by_attribute():
    coffee_df = pd.read_csv('pandas/coffee.csv')
    print(coffee_df.Day)
    print(coffee_df["Day"])


# Ordena os valores por coluna
def sorting_dataframe_values():
    coffee_df = pd.read_csv('pandas/coffee.csv')
    # print(coffee_df.sort_values("Units Sold"))
    # print(coffee_df.sort_values("Units Sold", ascending=False))
    print(coffee_df.sort_values(
        ["Units Sold", "Coffee Type"],
        ascending=[False, True]
        )
    )


# Possível, mas vai perder a performance de memória que o pandas proporciona
def iteranting_on_dataframe():
    coffee_df = pd.read_csv('pandas/coffee.csv')
    for index, row in coffee_df.iterrows():
        print(index)
        # print(row)
        print(row["Units Sold"])
        print("\n")


# get_specific_data_with_loc()
# change_dataframe_data()
# get_specific_data_with_at_iat()
# access_data_by_attribute()
# sorting_dataframe_values()
iteranting_on_dataframe()

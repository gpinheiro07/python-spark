import pandas as pd


# Trazer dados especificos baseado no valor de indexes e colunas
def filter_bios_data_index_and_columns():
    bios_df = pd.read_excel(
        "pandas/olympics-data.xlsx",
        sheet_name="bios"
    )
    # Aqui verificamos que altura e peso são floats
    # print(bios_df.info())

    # Obtém os atletas com altura maior que 2 metros e 15cm
    # print(bios_df.loc[bios_df["height_cm"] > 215])
    # print(bios_df.loc[bios_df["height_cm"] > 215, ["name", "height_cm"]])

    # Sintaxe um pouco menor com o mesmo resultado:
    # print(bios_df[bios_df["height_cm"] > 215][["name", "height_cm"]])
    print(bios_df[
            (bios_df["height_cm"] > 215) & (bios_df["born_country"] == "USA")
        ]
    )


# Filtrar dados verificando se a string contém algum valor específico
def filter_bio_data_with_str_operations():
    bios_df = pd.read_excel(
        "pandas/olympics-data.xlsx",
        sheet_name="bios"
    )
    # Também é possivel filtrar usando regex
    # print(bios_df[bios_df["name"].str.contains("gabriel|andré", case=False)])
    print(bios_df[bios_df["name"].str.startswith("Gabriel")])


#  Verifica se os valores do dataframe contidos em uma lista
def filter_bios_with_is_in():
    bios_df = pd.read_excel(
        "pandas/olympics-data.xlsx",
        sheet_name="bios"
    )
    # print(bios_df[bios_df["born_country"].isin(["USA", "FRA", "BR"])])
    print(bios_df[bios_df["born_country"].isin(["FRA", "BR"]) & (
        bios_df["name"].str.startswith("Gabriel")
    )])


# Outra maneira de filtrar dados
def using_query_method():
    bios_df = pd.read_excel(
        "pandas/olympics-data.xlsx",
        sheet_name="bios"
    )
    print(bios_df.query('born_country == "USA" and born_city == "Seattle"'))


# filter_bios_data_index_and_columns()
# filter_bio_data_with_str_operations()
# filter_bios_with_is_in()
using_query_method()

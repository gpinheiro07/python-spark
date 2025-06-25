"""
CSV (Comma Separated Values) é um arquivo de texto que utiliza
uma estrutura especifica para organizar dados tabulares, normalmente
a primeira linha identifica os dados e as linha subsequentes são dados
separados por um delimitador

Delimitadores comuns:
vírgula (,)
tab (/t)
dois pontos (:)
ponto e vírgula (;)

Parâmetros opcionais: delimiter, quotechar e escapechar

Problema comum:
Em um arquivo CSV, os campos geralmente são separados por vírgula. Mas às
    vezes o próprio conteúdo do campo tem uma vírgula (employee_addresses.csv),
    como em endereços.

delimiter -> define qual caractere separa os campos. O padrão é a vírgula (,).

quotechar -> define o caractere usado para cercar campos que contêm o
    delimitador. O padrão é aspas ("). Por exemplo: "Rua A, número 1"

escapechar -> define um caractere para escapar o delimitador dentro do campo.
    Por exemplo: Rua A\, número 1.

Importante:
Esses parâmetros não corrigem arquivos mal formatados. Eles funcionam apenas
    se o arquivo estiver organizado de forma compatível com o parâmetro usado.
    Se o CSV estiver bagunçado, talvez seja necessário corrigir o conteúdo
    primeiro.
"""


import csv


# Abre a lê os dados do arquivo com a biblioteca csv
def read_csv_file():
    with open('working_with_csv/employee_birthday.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department,\
                    and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines')


# Abre o arquivo csv como um dicionario (primeira linha = keys)
def read_csv_as_dict():
    with open('working_with_csv/employee_birthday.csv', 'r') as csv_file:
        # Caso não tiver as keys pode definir com o parametro 'fieldnames'
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["name"]} works in the {row["department"]}\
                department, and was born in {row["birthday month"]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')


# Lê um arquivo csv onde os valores possuem o mesmo delimitador (vírgula)
# Depende da formatação do csv
def read_comma_values_csv():
    with open('working_with_csv/employee_addresses.csv', 'r') as csv_file:
        _ = csv.reader(csv_file, delimiter=':')
        _ = csv.reader(csv_file, quotechar='"')
        _ = csv.reader(csv_file, escapechar='\\')

        # Resto da implementação


# read_csv_file()
read_csv_as_dict()
# read_comma_values_csv()

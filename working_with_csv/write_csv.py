"""
QUOTE_MINIMAL -> só coloca aspas nos campos que contêm o delimitador ou o
    caractere de aspas. (Padrão)
QUOTE_ALL -> coloca aspas em todos os campos.
QUOTE_NONNUMERIC -> coloca aspas apenas nos campos de texto e converte os
    numéricos para float.
QUOTE_NONE -> não usa aspas; em vez disso, escapa os delimitadores. Nesse caso,
    é obrigatório definir também o escapechar.

DictWriter -> parâmetro fieldnames é obrigatório
"""


import csv


# Cria um arquivo csv (sem header)
def write_csv_file():
    with open(
        'working_with_csv/employee_file.csv', mode='w', newline=''
    ) as csv_file:
        csv_writer = csv.writer(
            csv_file, delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow(['John Smith', 'Accounting', 'November'])
        csv_writer.writerow(['Erica Meyers', 'IT', 'March'])


# Cria um arquivo csv a partir de um dict
def write_csv_file_from_dict():
    with open(
        'working_with_csv/employee_file2.csv', mode='w', newline=''
    ) as csv_file:
        fieldnames = ['emp_name', 'dept', 'birth_month']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        csv_writer.writeheader()
        csv_writer.writerow(
            {
                'emp_name': 'John Smith',
                'dept': 'Accounting',
                'birth_month': 'November'
            }
        )
        csv_writer.writerow(
            {
                'emp_name': 'Erica Meyers',
                'dept': 'IT',
                'birth_month': 'March'
            }
        )


# write_csv_file()
write_csv_file_from_dict()

"""
Métodos de leitura de arquivo:
.read(size=-1) -> Lê o arquivo baseado no número de bytes
    (sem argumento, None ou -1 = arquivo inteiro é lido)
.readline(size=-1) -> Lê no máximo o número de caracteres da linha.
    Continua até o final da linha e retorna (sem argumento, None ou -1 =
    arquivo inteiro é lido = linha inteira é lida)
.readlines() -> Lê as linhas restantes do arquivo e retorna como lista
"""


# Lê todo o arquivo
def read_all_file() -> None:
    with open('reading_write_files/dog_breeds.txt', 'r') as reader:
        print(reader.read())


# Lê os primeiros 5 caracteres da linha 5 vezes
def read_line_bytes() -> None:
    with open('reading_write_files/dog_breeds.txt', 'r') as reader:
        print(reader.readline(5))
        print(reader.readline(5))
        print(reader.readline(5))
        print(reader.readline(5))
        print(reader.readline(5))


# Lê o arquivo e salva em uma lista (linha = posição)
def read_lines_as_list(mode: int = 0) -> None:
    with open('reading_write_files/dog_breeds.txt', 'r') as reader:
        if mode == 0:
            print(reader.readlines())
        else:
            # Também pode ser feito transformando o objeto do arquivo em lista
            print(list(reader))


# Itera sobre as linhas do arquivo
def iterating_over_lines(mode: int = 0) -> None:
    with open('reading_write_files/dog_breeds.txt', 'r') as reader:
        if mode == 0:
            line = reader.readline()
            while line != '':  # EOF é uma string vazia
                print(line, end='')
                line = reader.readline()
        elif mode == 1:
            # Utilizando o readlines (lista de linhas)
            for line in reader.readlines():
                print(line, end='')
        else:
            # Iterando sobre o próprio objeto (mais rapido e eficiente)
            for line in reader:
                print(line, end='')


# read_all_file()
# read_line_bytes()
# read_lines_as_list(mode=1)
# iterating_over_lines(mode=2)

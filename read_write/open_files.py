"""
Estrutura de um arquivo:
Header -> metadados sobre o conteúdo do arquivo
Data -> conteúdo do arquivo
End of file (EOF) -> Caracter especial que indica fim do arquivo

Modos de abertura (mais comuns):
r -> apenas leitura (padrão)
w -> escrita (sobrescreve o arquivo)
rb / wb -> modo binário (leitura / escrita)
"""


# Criando objeto do arquivo e fechando o arquivo
def open_close_file():
    file = open('text_file.txt')
    file.close()


# Usando context manager para fechar o arquivo automaticamente
def open_with_context():
    with open('text_file.txt') as _:
        ...


#  Define o modo como quer trabalhar com o arquivo
def open_file_mode():
    with open('text_file.txt', 'r') as _:
        ...

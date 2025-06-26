"""
Métodos de escrita de arquivo:
.write -> Escreve a string no arquivo
.writelines(seq) -> Escreve em sequencia no arquivo, não adiciona nenhuma
    terminação de linha
"""


# Inverte a posição das linhas no arquivo
def write_in_file(mode: int = 0):
    with open('reading_write_files/dog_breeds.txt', 'r') as reader:
        breeds = reader.readlines()

    with open('reading_write_files/dog_breeds.txt', 'w') as writer:
        if mode == 0:
            for breed in reversed(breeds):
                writer.write(breed)
        else:
            writer.writelines(reversed(breeds))


write_in_file(mode=1)

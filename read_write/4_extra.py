# Pega o caminho de onde o script foi executado com __file__
def get_path():
    print(__file__)


# Adiciona ao final do arquivo sem sobrescrever
def append_file():
    with open('reading_write_files/dog_breeds.txt', 'a') as a_writer:
        a_writer.write('\nBeagle')


# Trabalhando com dois arquivos simultaneos
def open_two_files():
    d_path = 'reading_write_files/dog_breeds.txt'
    d_r_path = 'reading_write_files/dog_breeds_reversed.txt'
    with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
        dog_breeds = reader.readlines()
        writer.writelines(reversed(dog_breeds))


# get_path()
# append_file()
open_two_files()

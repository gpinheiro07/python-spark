"""
Script que converte arquivos com finais de linhas tipo DOS (\r\n) para
para finais de linha tipo Unix(\n).
"""

import argparse
import os


# Converte o final da string de \r\n para \n
def str2unix(input: str) -> str:
    r_str = input.replace('\r\n', '\n')
    return r_str


# Converte arquivo DOS para Unix
def dos2unix(source_file: str, dest_file: str) -> None:
    with open(source_file, 'r') as reader:
        dos_content = reader.read()

    unix_content = str2unix(dos_content)

    with open(dest_file, 'w') as writer:
        writer.write(unix_content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script que converte arquivo DOS para Unix"
    )

    parser.add_argument(
        'source_file',
        help='Caminho do arquivo base'
    )

    parser.add_argument(
        '--dest_file',
        help='Caminho do arquivo de destino',
        default=None
    )

    args = parser.parse_args()
    s_file = args.source_file
    d_file = args.dest_file

    if d_file is None:
        file_path, file_extension = os.path.splitext(s_file)
        d_file = f'{file_path}_unix{file_extension}'

    dos2unix(s_file, d_file)

"""
Validador de JSON pelo terminal atráves do Python json.tool:
python -m json.tool dog_friend.json
python -m json.tool dog_friend.json --indent 2 -> exibir com identação
python -m json.tool dog_friend.json --compact -> remove os espaços em branco

Importante: deixar um JSON formatado e bonito com espaços em branco aumenta o
    tamanho dele e pode ser um problema ao trabalhar com JSON muito grande
"""


import json


dog_friend = {
    "name": "Mitch",
    "age": 6.5,
}


# Define identação do JSON-string por número de espaços (Padrão = None)
def indent_json_dumps():
    print(json.dumps(dog_friend))

    # Para pular de linha
    print(json.dumps(dog_friend, indent=0))
    print(json.dumps(dog_friend, indent=""))

    # Não muito útil mas possível
    print(json.dumps(dog_friend, indent=-2))
    print(json.dumps(dog_friend, indent=" ⮑ "))

    # Mais comum
    print(json.dumps(dog_friend, indent=2))
    print(json.dumps(dog_friend, indent=4))


def ident_json_dump():
    with open(
        'working_with_json/dog_friend.json', mode='w', encoding='utf-8'
    ) as json_file:
        json.dump(dog_friend, json_file, indent=4)


# Replica o comportamento do json.tools --compact
def minify_json():
    with open(
        'working_with_json/hello_frieda.json', mode='r', encoding='utf-8'
    ) as input_json_file:
        # Poderia usar json.load diretamente para pegar o arquivo
        original_json = input_json_file.read()

        json_data = json.loads(original_json)
        # Poderia usar json.dump diretamente para salvar o arquivo
        # separators -> remove os espaços após vírgula e dois pontos
        # (Padrão (", ", ": "))
        mini_json = json.dumps(json_data, indent=None, separators=(",", ":"))

        with open(
            "working_with_json/mini_frieda.json", mode="w", encoding="utf-8"
        ) as output_json_file:
            output_json_file.write(mini_json)

        print(json_data)
        print(mini_json)


# indent_json_dumps()
# ident_json_dump()
minify_json()

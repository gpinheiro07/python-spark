"""
JSON não suporta aspas simples ('), comentários e vírgula final

HJSON / JSONC -> Permitem algumas formatações a mais sendo JSONC mais estrito

Tipos de dado suportado:
object ->	par de chave-valor dentro de colchetes ({})
array ->	lista de valores dentro de chaves ([])
string ->	texto dentro de aspas duplas ("")
number ->	inteiros ou floats
boolean ->	true ou false (sem aspas)
null ->	valor nulo

Serialização -> converter dados para o formato JSON
Desserialização -> decodificar dados JSON para um formato utilizável em python

Python-JSON (de-para):
dict    ->	 object
list    ->	 array
tuple   ->	 array
str     ->	 string
int     ->	 number
float   ->   number
True    -> 	 true
False   ->   false
None    -> 	 null
"""


import json


# json.dumps -> converte um dicionário python para uma string com formato JSON
# não cria um tipo de dado JSON diretamente
def convert_dict_to_json():
    food_ratings = {"organic dog food": 2, "human food": 10}
    print(json.dumps(food_ratings))

    # Ao converter para uma JSON-string as chaves sempre serão strings
    numbers_present = {1: True, 2: True, 3: False}
    print(json.dumps(numbers_present))


# Converte tipos de dados diferentes para o tipo JSON
def convert_data_types_to_json():
    print(json.dumps(True))
    print(json.dumps(("eating", "sleeping", "barking")))


# dicionários, listas e tuplas não podem ser usados como chaves de um json,
# pois as keys devem ser strings.
# dicionários, listas e sets -> não podem ser tranformados em keys
# (sem hash e mutáveis)
def use_tuple_as_json_key():
    available_nums = {(1, 2): True, 3: False}
    # TypeError: keys must be str, int, float, bool or None, not tuple
    print(json.dumps(available_nums))
    # Ignora valores não suportados pelo JSON
    print(json.dumps(available_nums, skipkeys=True))


# organiza as chaves alfabeticamente
def sort_json_string():
    toy_conditions = {"chew bone": 7, "ball": 3, "sock": -1}
    print(json.dumps(toy_conditions, sort_keys=True))


# json.dump -> salva dados em python em um arquivo tipo JSON
def write_json_into_file():
    dog_data = {
        "name": "Frieda",
        "is_dog": True,
        "hobbies": ["eating", "sleeping", "barking",],
        "age": 8,
        "address": {
            "work": None,
            "home": ("Berlin", "Germany",),
        },
        "friends": [
            {
                "name": "Philipp",
                "hobbies": ["eating", "sleeping", "reading",],
            },
            {
                "name": "Mitch",
                "hobbies": ["running", "snacking",],
            },
        ],
    }
    with open(
        'working_with_json/hello_frieda2.json', mode='w', encoding='UTF-8'
    ) as json_file:
        json.dump(dog_data, json_file)


# convert_dict_to_json()
# convert_data_types_to_json()
# sort_json_string()]
write_json_into_file()

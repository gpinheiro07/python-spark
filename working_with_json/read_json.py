"""
json.loads -> Para desserealizar instancias de string, byte ou array de bytes:
json.load -> Para desserealizar arquivos de texto ou binarios

Usar loads quandos os dados já estão presentes no seu arquivo Python
Usar load com arquivos externos salvos no disco

"""

import json


# Desserealização não é o exato oposto de serialização,
# pois nem todos os tipos suportados por Python são suportados pelo JSON
def serialize_deserealize_json():
    dog_registry = {1: {"name": "Frieda"}}
    dog_json = json.dumps(dog_registry)
    new_dog_registry = json.loads(dog_json)
    print(dog_registry)
    print(new_dog_registry)

    dog_data = {
        "name": "Frieda",
        "is_dog": True,
        "hobbies": ["eating", "sleeping", "barking",],
        "age": 8,
        "address": {
            "work": None,
            "home": ("Berlin", "Germany",),
        },
    }
    dog_data_json = json.dumps(dog_data)
    print(dog_data_json)
    new_dog_data = json.loads(dog_data_json)
    print(new_dog_data)
    print(type(dog_data["address"]["home"]))
    print(type(new_dog_data["address"]["home"]))


def read_json_file():
    with open(
        'working_with_json/hello_frieda2.json', mode='r', encoding='UTF-8'
    ) as json_file:
        frie_data = json.load(json_file)
        print(frie_data['name'])


# serialize_deserealize_json()
read_json_file()

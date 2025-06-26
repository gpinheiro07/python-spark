import json


BASE_PATH = "playground/"


class JSONToText:
    def __init__(self) -> None:
        self._people_json = self._get_json_data()

    def _get_json_data(self) -> dict:
        with open(
            f"{BASE_PATH}people.json", mode="r", encoding="UTF-8"
        ) as json_file:
            return json.load(json_file)

    def save_names_on_file(self) -> None:
        with open(
            f"{BASE_PATH}people_name.txt", mode="w", encoding="UTF-8"
        ) as text_file_writer:
            for person in self._people_json:
                text_file_writer.write(person["nome"] + "\n")


json_to_text = JSONToText()
json_to_text.save_names_on_file()

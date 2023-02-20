import copy
from datetime import datetime
import json
import os


class Temp_data:
    def __init__(self):
        self.__str_json = self.load_json()
        # json_string = 

    def load_json(self) -> dict:
        if not os.path.exists('note.json'):
            with open ('note.json', 'w') as file:
                json.dump(self.__empty_pattern(), file, indent=2)
                print('файл создан')
            
        with open ('note.json', 'r') as file:
            print('файл открыт')
            return json.load(file)
        
    def get_str_json(self) -> dict:
        return copy.deepcopy(self.__str_json)

    def __empty_pattern (self):
        str_json = {"notes": [{}]}
        str_json["notes"][0]["id"] = 0
        str_json["notes"][0]["title"] = "new"
        str_json["notes"][0]["notation"] = "первая заметка"
        str_json["notes"][0]["time_create"] = datetime.now().strftime('%Y/%m/%d %H:%M')
        str_json["notes"][0]["time_change"] = datetime.now().strftime('%Y/%m/%d %H:%M')
        return str_json
    
    def add_new_note(self, title, notation):
        self.__str_json['notes'].append(self.__empty_pattern()['notes'][0])
        lenght = len(self.__str_json['notes'])
        self.__str_json['notes'][lenght-1]["id"] = self.__str_json['notes'][lenght-2]["id"] + 1
        self.__str_json['notes'][lenght-1]["title"] = title
        self.__str_json['notes'][lenght-1]["notation"] = notation
        self.__save_file()

    def amend_note (self, position, new_note):
        self.__str_json['notes'][position] = new_note
        self.__save_file()

    def delete_note(self, position):
        del self.__str_json['notes'][position]
        self.__save_file()


    def __save_file(self):
        with open ('note.json', 'w') as file:
            json.dump(self.__str_json, file, indent=2)

if __name__ == "__main__":
    print('123')
    test = Temp_data()
    print(test.str_json)
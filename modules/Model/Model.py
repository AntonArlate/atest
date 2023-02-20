import json
import modules
from .Temp_data import Temp_data

class Model:
    def __init__(self):
        print ('Model init')
        pass

    def set_presenter(self, presenter):
        self.presenter : modules.Presenter = presenter
        print (self.presenter, ' - установлен в Model')

    def preload_data(self):
        self.temp_data = Temp_data()




    def get_data (self, start, end, *filters):
        notes = self.__reqest_data_as_notes()
        if end == -1:
            end = len(notes)-1
        
        if start == -1:
            start = end
        
        notes = notes[start:end+1]
        i = 0
        # читаем все поля
        for note in notes:
            new = {}
            for k, v in note.items():
                if k in filters:
                    new[k] = v
            notes[i] = new
            i += 1

        return notes
    
    
    def get_field_search(self, field, value):
        notes = self.__reqest_data_as_notes()
        i = 0
        flag = False
        for note in notes:
            if note[field] == value:
                flag = True
                break
            i += 1

        if flag == True: return i
        else: return -1
    
    
    def add_new_note(self, title, notation):
        self.temp_data.add_new_note(title, notation)
        return True


    def __reqest_data_as_notes(self) -> list[dict]:
        data = self.temp_data.get_str_json()
        return data["notes"]
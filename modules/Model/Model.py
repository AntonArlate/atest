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
        data = self.temp_data.get_str_json()
        notes : list[dict] = data["notes"]
        if end == -1:
            end = len(notes)
        
        notes = notes[start:end]
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
    
    
    def add_new_note(self, title, notation):
        self.temp_data.add_new_note(title, notation)
        return True
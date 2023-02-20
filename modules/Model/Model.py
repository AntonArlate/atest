import datetime
from functools import reduce
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

        if filters == ():
            filters = (*notes[0],)
        
        notes = notes[start:end+1]
        i = 0
        # читаем все поля
        for note in notes:
            new = {}
            for k, v in note.items():
                # Выбираем запрошеные поля
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
    
    def delete_note(self, position):
        self.temp_data.delete_note(position)

    def amend_note(self, position, new_note):
        # new_note = {}
        # reduce(lambda first, second: new_note.update(second), change_fields, {})

        #перед попыткой изменения нам надо получить оригинал и попытаться переписать поля
        current_note = self.get_data(-1, position)
        new_note = {**current_note[0], **new_note}
        new_note["time_change"] = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
        self.temp_data.amend_note(position, new_note)

    def find_index_in_date (self, start_date : datetime, end_date : datetime):
        notes = self.get_data (0, -1, "time_create")

        #поиск стартового
        i = 0
        start_i = i
        for note in notes:
            note_date = list(map(lambda x: int(x), note["time_create"][0:10].split("/")))
            note_date = datetime.date(*note_date)
            if start_date < note_date:
                start_i = i
                break
            i += 1

        #поиск конечного
        i = len(notes)-1
        end_i = i
        for note in notes[-1::-1]:
            note_date = list(map(lambda x: int(x), note["time_create"][0:10].split("/")))
            note_date = datetime.date(*note_date)
            if end_date > note_date:
                end_i = i
                break
            i -= 1
        
        return start_i, end_i
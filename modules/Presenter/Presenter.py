import modules


class Presenter:

    def __init__(self):
        print ('Presenter init')
        view : modules.View
        pass

    def set_view(self, view):
        self.view : modules.View = view
        print (self.view, ' - установлен в Presenter')

    def set_model(self, model):
        self.model : modules.Model = model
        print (self.model, ' - установлен в Presenter')
        

    def start_view(self):
        self.view.menu_main()


    def preload_data(self):
        self.model.preload_data()
    
    def get_data(self, start, end, *filter):
        return self.model.get_data(start, end, *filter)
    
    def add_new_note(self, title, notation):
        return self.model.add_new_note(title, notation)
    
    def get_field_search(self, field, value):
        return self.model.get_field_search(field, value)
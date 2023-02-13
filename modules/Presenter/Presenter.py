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
        
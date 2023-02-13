import modules

class Model:
    def __init__(self):
        print ('Model init')
        pass

    def set_presenter(self, presenter):
        self.presenter : modules.Presenter = presenter
        print (self.presenter, ' - установлен в Model')
import modules


class View:
    def __init__(self):
        print ('View init')
        pass

    def set_presenter(self, presenter):
        self.presenter : modules.Presenter = presenter
        print (self.presenter, ' - установлен в View')


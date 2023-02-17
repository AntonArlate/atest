# Модуль - точка входа


import modules

def main():
    # print ('main run')
    view = modules.View()
    presenter = modules.Presenter()
    model = modules.Model()

    view.set_presenter(presenter)

    presenter.set_view(view)
    presenter.set_model(model)

    model.set_presenter(presenter)

    #запрос на импорт файла
    presenter.preload_data()

    #передача управления в Viever
    presenter.start_view()

if __name__ == "__main__":
    main()


    
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


if __name__ == "__main__":
    main()


    
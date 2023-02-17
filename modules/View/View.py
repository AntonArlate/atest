import modules


class View:
    def __init__(self):
        print ('View init')
        pass

    def set_presenter(self, presenter):
        self.presenter : modules.Presenter = presenter
        print (self.presenter, ' - установлен в View')

    def menu_main(self):
    
        begin = True
        while begin:
            
            print ('------ \n Введите число для соответствующей задачи или иное для выхода: ')
            print ('   0.\t Отобразить весь список заметок')
            print ('   1.\t Добавить заметку')
            print ('   2.\t ')
            print ('   3.\t ')
            print ('   4.\t ')

            program = int(input())
            print ()
            
            #Отобразить весь список заметок
            if program == 0:
                # Viewer запрашивает диапозон и фильтр для данных. В ответ получает список отфильтрованных словарей
                # -1 start = извлечь одну позициюуказанную в end
                # -1 end = извлечь до последней
                reqest_field = ('id', 'time_create', 'title')
                data = self.presenter.get_data(0, -1, *reqest_field)

                
                for i in range(len(reqest_field)):
                    if i == 0: a="{:^3}"
                    if i == 1: a="{:17}"
                    if i == 2: a="{:}"

                    print(a.format(reqest_field[i]), end='')

                print()
                for item in data:
                    for i in range(len(reqest_field)):
                        if i == 0: a="{:^3}"
                        if i == 1: a="{:17}"
                        if i == 2: a="{:}"
                        print(a.format(item[reqest_field[i]]), end='')
                    print()

            #Добавить заметку
            elif program == 1:
                print("следуйте инструкции конструктора:")
                                
                title = input('Введите заголовок. Или оставте пустым для "new note"')
                if title == "":
                    title = "new note"
                
                notation = input('Введите заметку. Или оставте пустым для "empty note"')
                if notation == "":
                    notation = "empty"
                   
                if self.presenter.add_new_note(title, notation):
                    print("Заметка успешно создана")
                else: print ("Заметка не была создана по неизвестной причине")

            elif program == 2:
                form = export_proces(data)
                if form != 0:
                    input(f'Данные экспортированы в формате {form} \nЧтобы продолжить, нажмите Enter.')
                else: input(f'Не известный формат \nЧтобы продолжить, нажмите Enter.')

            elif program == 3:
                redactor_menu()

            elif program == 4:
                find_process()       


            else:
                begin = False
                break
            
            print()
            input(f'<<< Press enter >>>')
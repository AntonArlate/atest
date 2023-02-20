import datetime
import modules


class View:
    def __init__(self):
        print ('View init')
        pass

    def set_presenter(self, presenter):
        self.presenter : modules.Presenter = presenter
        print (self.presenter, ' - установлен в View')

    def menu_main(self):
        last_id = -1
    
        begin = True
        while begin:
            
            print ('------ \n Введите число для соответствующей задачи или иное для выхода: ')
            print ('   0.\t Отобразить весь список заметок')
            print ('   1.\t Добавить заметку')
            print ('   2.\t Отобразить заметку')
            print ('   3.\t Список с выборкой по дате создания')

            program = input()
            print ()
            
            #Отобразить весь список заметок
            if program == "0":
                # Viewer запрашивает диапазон и фильтр для данных. В ответ получает список отфильтрованных словарей
                # -1 start = извлечь одну позициюуказанную в end
                # -1 end = извлечь до последней
                self.view_list(0, -1)

            #Добавить заметку
            elif program == "1":
                print("следуйте инструкции конструктора:")
                                
                title = input('Введите заголовок. Или оставте пустым для "new note"\n')
                if title == "":
                    title = "new note"
                
                notation = input('Введите заметку. Или оставте пустым для "empty note"\n')
                if notation == "":
                    notation = "empty"
                   
                if self.presenter.add_new_note(title, notation):
                    print("Заметка успешно создана")
                else: print ("Заметка не была создана по неизвестной причине")

            #Отобразить заметку
            elif program == "2":
                id = input('Введите ID заметки. Или оставте пустым для выбора последней\n')
                if not id == "":
                    # запрашиваем поиск зачения в поле "id" 
                    data_pos = self.presenter.get_field_search("id", int(id))
                else: data_pos = last_id
                
                if not data_pos == -1:
                    # запрашиваем заметку
                    reqest_field = ('id', 'time_create', 'time_change', 'title', 'notation')
                    data = self.presenter.get_data(-1, data_pos, *reqest_field)
                    print(f"\
id: {data[0]['id']}\n\
Время создания: {data[0]['time_create']}\n\
Последнее изменение: {data[0]['time_change']}\n\n\
{data[0]['title']}\n\n\
{data[0]['notation']}")

                    last_id = id
                    input('<<< Press enter >>>')
                    self.menu_note(data, data_pos)
                    
                else: print("заметка не найдена")

            #выборка по дате
            elif program == "3":
                print("следуя инструкции введите значения: ")
                start_d = input('Нач. год (пусто для 1): ')
                if start_d == "": 
                    start_date = datetime.date(1,1,1)
                else:
                    start_date = datetime.date(int(start_d), 1, 1)
                    start_d = input('Нач. мес (пусто для 1): ')
                    if start_d == "":
                        pass
                    else:
                        start_date = datetime.date(start_date.year, int(start_d), 1)
                        start_d = input('Нач. день (пусто для 1): ')
                        if start_d == "": 
                            pass
                        else:
                            start_date = datetime.date(start_date.year, start_date.month, int(start_d))

                today = datetime.date.today()
                end_d = input('Кон. день (пусто для сегодня): ')
                if end_d == "": 
                    end_date = today
                else:
                    end_date = datetime.date(today.year, 12, int(end_d))
                    end_d = input('Кон. мес (пусто для текущий): ')
                    if end_d == "":
                        end_date = datetime.date(today.year, today.month, end_date.day)
                    else:
                        end_date = datetime.date(today.year, int(end_d), end_date.day)
                        end_d = input('Кон. год (пусто для текущий): ')
                        if end_d == "":
                            pass
                        else: 
                            end_date = datetime.date(int(end_d), end_date.month, end_date.day)

                # запрашиваем поиск индексов
                index = self.presenter.find_index_in_date(start_date, end_date)
                #запрашиваем список из диапозона
                self.view_list(*index)

            else:
                begin = False
                break
            
            print()
            input('<<< Press enter >>>')


    def view_list(self, start_i, end_i):
        reqest_field = ('id', 'time_create', 'title')
        data = self.presenter.get_data(start_i, end_i, *reqest_field)

        for i in range(len(reqest_field)):
            if i == 0: a="{:^3}" #для оптимизации в дальнейшем можно сделать в виде листа строк
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

    def menu_note(self, data, data_pos):
    
        begin = True
        while begin:
            
            print ('------ \n Введите число для соответствующей задачи или иное для перехода назад: ')
            print ('   0.\t Удалить')
            print ('   1.\t Изменить')

            program = input()
            print ()
            
            #Удалить заметку
            if program == "0":
                if input('УДАЛИТЬ? (y): ').lower() == "y":
                    # отправляем запрос на удаление
                    self.presenter.delete_note(data_pos)
                    print('Выполнено')
                    break

            elif program == "1":
                print("следуйте инструкции конструктора:")
                                
                title = input('Введите заголовок. Или оставте пустым для пропуска\n')
                if title == "":
                    title = data[0]['title']
                else: data[0]['title'] = title
                
                notation = input('Введите заметку. Или оставте пустым для пропуска\n')
                if notation == "":
                    notation = data[0]['notation']
                else: data[0]['notation'] = notation

                # отправляем запрос на изменение
                # функция принимает словарь, для простоты отправляем всю изменённую заметку
                self.presenter.amend_note(data_pos, data[0])
               
            else:
                begin = False
                break
            
            print()
            input('<<< Press enter >>>')
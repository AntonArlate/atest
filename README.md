# Программа для заметок в качестве учебного проекта.
## Навигация по модулям
[main.py](/main.py) - Точка входа. Инициирует все классы и передаёт управление в [View.py](/modules/View/View.py)

[View.py](/modules/View/View.py) - Вьюшка. Онже пользовательский интерфейс. Общается с пользователем и посылает запросы в обработчик через [Presenter.py](/modules/Presenter/Presenter.py)

[Presenter.py](/modules/Presenter/Presenter.py) - Связующий интерфейс (сами интерфейсы не реализованы)

[Model.py](/modules/Model/Model.py) - основная backend логика программы. Ловит запросы от UI и работает с репозиторием [Temp_data.py](/modules/Model/Temp_data.py)

[Temp_data.py](/modules/Model/Temp_data.py) - Импровизированый репозиторий. Отвечает за работу с файлом и хранение загруженной информации.

[note.json](/note.json) - файл в формате .json для хранения данных. При отсутствии создаётся автоматически с нулевой записью.
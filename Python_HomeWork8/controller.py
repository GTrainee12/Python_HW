from import_data import import_data
from export_data import export_data
from employee_search import employee_search
from editing_info import editing_info

def greeting():
    print("Добро пожаловать в систему управления персоналом!")


def choice_todo():
    print("Доступные операции с системой управления персоналом:\n\
    1 - Ввод сотрудника в систему:\n\
    2 - Открытие базы сотрудников:\n\
    3 - Поиск сотрудника:\n\
    4 - Редактирование данных сотрудника:"
          )
    ch = input("Введите цифру: ")
    match ch:
        case "1":
            import_data()
        case "2":
            export_data()
        case "3":
            employee_search()
        case "4":
            editing_info()
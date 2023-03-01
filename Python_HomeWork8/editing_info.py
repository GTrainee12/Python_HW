# модуль редактирования данных
import openpyxl

def editing_info():
    staff_book = openpyxl.open("Staff_book.xlsx")
    sheet = staff_book.active
    id = int(input("Введите id сотрудника для поиска: "))
    print("ID:".center(1), "ФИО:".center(35), "Отдел:".center(20), "Должность:".center(25), "Телефон:".center(10), "Рейтинг:".center(15), "Колличество рабочих дней:".center(10))
    for row in sheet.iter_rows(min_row = id, max_row = id, min_col= 1, max_col=7):
        for cell in row:
            print(cell.value, end = '       ')
        print()



    print("Доступные данные для редактирования:\n\
        1 - Ф.И.О.:\n\
        2 - Отдел сотрудника:\n\
        3 - Должность сотрудника:\n\
        4 - Номер телефона сотрудника:\n\
        5 - Рабочий рейтинг сотрудника:\n\
        6 - Колличество рабочих дней:\n\
        7 - Удаление сотрудника:"

          )
    editing = int(input("Что будем редактировать ? : "))
    match editing:
        case 1:
                last_name = input("Введите фИО сотрудника: ")
                sheet[id][1].value = last_name
        case 2:
            note = input("Введите отдел сотрудника: ")
            sheet[id][2].value = note
        case 3:
            post = input("Введите должность: ")
            sheet[id][3].value = post
        case 4:
            phone_number = input("Введите номер телефона сотрудника: ")
            sheet[id][4].value = phone_number
        case 5:
            rating = input("Введите рабочий рейтинг сотрудника: ")
            sheet[id][5].value = rating
        case 6:
            working_days = input("Введите колличество рабочих дней: ")
            sheet[id][6].value = working_days
        case _:
            sheet[id][0].value = None
            sheet[id][1].value = None
            sheet[id][2].value = None
            sheet[id][3].value = None
            sheet[id][4].value = None
            sheet[id][5].value = None
            sheet[id][6].value = None
    staff_book.save("Staff_book.xlsx")
    staff_book.close()
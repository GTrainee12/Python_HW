# модуль экспорта данных
import openpyxl

def employee_search():
    staff_book = openpyxl.open("Staff_book.xlsx", read_only=True)
    sheet = staff_book.active
    id = int(input("Введите id сотрудника для поиска: "))
    print("ID:".center(1), "ФИО:".center(35), "Отдел:".center(10), "Должность:".center(25), "Телефон:".center(15), "Рейтинг:".center(20), "Колличество рабочих дней:".ljust(5))


    for row in sheet.iter_rows(min_row = id, max_row = id, min_col= 1, max_col=7):
        for cell in row:
            print(cell.value, end = '       ')
        print()
    print("-"*140)
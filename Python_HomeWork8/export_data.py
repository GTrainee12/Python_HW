# модуль поиска данных
import openpyxl
def export_data():
    staff_book = openpyxl.open("Staff_book.xlsx", read_only=True)
    sheet = staff_book.active

    print("ID:".center(1), "ФИО:".center(35), "Отдел:".center(20), "Должность:".center(40), "Телефон:".center(15), "Рейтинг:".center(20), "Колличество рабочих дней:".center(15))


    for row in range(1,sheet.max_row+1):
        id = sheet[row] [0].value
        last_name = sheet[row] [1].value
        note = sheet[row] [2].value
        post = sheet[row] [3].value
        phone_number = sheet[row] [4].value
        rating = sheet[row] [5].value
        working_days = sheet[row] [6].value
        id, last_name, note, post, phone_number, rating, working_days
        print(f"{id}".center(1),F"{last_name}".center(42), f"{note}".ljust(30), f"{post}".ljust(25), f"{phone_number}".ljust(25), F"{rating}".ljust(15), F" {working_days} ".ljust(10))
    print("-"*140)
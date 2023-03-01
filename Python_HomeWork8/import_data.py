# модуль импорта данных
import openpyxl


def import_data():
    id = int(input("Введите id сотрудника : "))
    last_name = input("Введите фИО сотрудника: ")
    note = input("Введите отдел сотрудника: ")
    post = input("Введите должность: ")
    phone_number = input("Введите номер телефона сотрудника: ")
    rating = input("Введите рабочий рейтинг сотрудника: ")
    working_days = input("Введите колличество рабочих дней: ")
    [id,last_name, note, post, phone_number, rating, working_days]
    staff_book = openpyxl.open("Staff_book.xlsx")
    sheet = staff_book.active
    sheet.append([id,last_name, note, post, phone_number, rating, working_days])
    staff_book.save("Staff_book.xlsx")
    staff_book.close()


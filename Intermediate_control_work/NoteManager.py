from Note import *


def greeting():
    print("Добро пожаловать в систему заметок!")
def main():


    while True:
        print("1. Добавить заметку")
        print("2. Посмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            list_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Неверный выбор!")
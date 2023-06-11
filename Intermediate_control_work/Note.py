import json
import datetime

notes = []

# функция добавления заметки
def add_note():
    note = {}
    note['id'] = len(notes) + 1
    note['title'] = input("Введите заголовок: ")
    note['body'] = input("Введите текст заметки: ")
    note['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    notes.append(note)
    save_notes()

# функция вывода списка заметок
def list_notes():
    for note in notes:
        print(f"{note['id']}: {note['title']} - {note['body']} [{note['timestamp']}]")

# функция редактирования заметки
def edit_note():
    note_id = int(input("Введите идентификатор заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок: ")
            note['body'] = input("Введите новый текст заметки: ")
            note['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            break
    else:
        print("Заметка не найдена!")
    save_notes()

# функция удаления заметки
def delete_note():
    note_id = int(input("Введите идентификатор заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            break
    else:
        print("Заметка не найдена!")
    save_notes()

# функция сохранения заметок
def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

# функция чтения заметок
def load_notes():
    global notes

    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        pass
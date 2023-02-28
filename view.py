import datetime


def get_mode() -> int:
    print("=" * 20)
    print("Выберите необходимое действие: ")
    print("1. Создать Записку")
    print("2. Вывести список всех Записок")
    print("3. Найти Записки по датам")
    print("4. Найти и вывести Записку на экран")
    print("5. Редактировать Записку")
    print("6. Удалить Записку")
    print("7. Закончить работу")
    print("=" * 20 + "\n")
    return int(input("Введите номер необходимого действия: "))


def get_add_new_note():
    print("Введите данные: ")
    new_note = []
    temp = {}
    temp["id_note"] = "temp"
    temp["title_note"] = input("Введите заголовок: ")
    temp["text_note"] = input("Введите текст: ")
    temp["date_note"] = datetime.datetime.now()
    new_note.append(temp)
    return new_note


def print_to_screen(notes_arr: list):
    for note in notes_arr[:]:
        print("ID    - " + note[0])
        print("Title - " + note[1])
        print("Text  - " + note[2])
        print("Date  - " + note[3])


def input_message(prompt) -> str:
    return input(prompt + ": ")


def put_message(promt):
    print(promt)

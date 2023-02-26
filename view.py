import datetime

def get_mode() -> int:
    print("=" * 20)
    print("Выберите необходимое действие: ")
    print("1. Создать Записку")
    print("2. Вывести список всех Записок")
    print("3. Найти Записки по датам")
    print("4. Вывести Записку на экран")
    print("5. Редактировать записку")
    print("6. Закончить работу")
    print("=" * 20+ "\n")
    return int(input("Введите номер необходимого действия: "))

def get_add_new_note():
    print("\n" + "-" * 20)
    print("Введите Записку: ")
    new_note = []
    temp = {}
    temp["id_note"] = "temp"
    temp["title_note"] = input("Введите заголовок: ")
    temp["text_note"] = input("Введите текст: ")
    temp["date_note"] = datetime.datetime.now()
    new_note.append(temp)
    return new_note

def print_to_screen(notes_arr: list):
    print("\n" + "-" * 20)
    print("Список записок: \n")
    print("ID    Title    Text    DateTime\n")
    for note in notes_arr[:]:
        print(note[0] + "    " + note[1] + "    " + note[2] + "    " + note[3])
   

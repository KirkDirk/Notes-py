import datetime
import view as view
import file_work as fw


def start_notes():
    while True:
        mode = view.get_mode()
        if mode == 1:
            view.put_message("\nВносим Записку:")
            data_new_note = view.get_add_new_note()
            fw.append_to_csv(fw.get_last_id(), data_new_note)
            view.put_message("Записка добавлена")

        elif mode == 2:
            data_notes = fw.read_csv()
            view.put_message("\nСписок всех записок: \n")
            view.print_to_screen(data_notes)

        elif mode == 3:
            view.put_message("\nИщем Записки по датам:")
            start_date = datetime.datetime.strptime(view.input_message("\nВведите начальную дату (дд/мм/гггг )"), "%d/%m/%Y")
            end_date = datetime.datetime.strptime(view.input_message("\nВведите конечную дату (дд/мм/гггг )"), "%d/%m/%Y")
            view.put_message("\nНайденные по датам Записки: \n")
            view.print_to_screen(find_notes_by_dates(start_date, end_date))

        elif mode == 4:
            view.put_message("\nИщем Записку и выводим ее на экран:\n")
            find_note(view.input_message("Введите искомое"))

        elif mode == 5:
            view.put_message("Редактируем Записку:\n")
            old_id = view.input_message("Введите ID")
            new_note = view.get_add_new_note()
            fw.replacement_note(new_note, old_id)
            view.put_message("Данные сохранены")

        elif mode  == 6:
            view.put_message("Удаляем Записку:\n")
            del_id = view.input_message("Введите ID")
            new_note = find_note_by_id(del_id)
            new_note[0]["title_note"] = "Note deleted"
            new_note[0]["text_note"] = "null"
            fw.replacement_note(new_note, del_id)
            view.put_message("Данные удалены")

        elif mode == 7:
            view.put_message('Всего хорошего!\n')
            break
        print('\nДальше?\n')


def find_note(find_data):
    notes_data = fw.read_csv_to_arr()
    found_list = []
    for line in notes_data:
        for elem in line:
            if find_data in elem:
                found_list.append(line)
                break
    if found_list > []:
        view.put_message('\nНайденные записки ():\n')
        view.print_to_screen(found_list)
    else:
        view.put_message('Искомое не найдено')
    return

def find_note_by_id(num_id) -> list:
    notes_data = fw.read_csv()
    found_list = []
    for note in notes_data:
        if num_id == note["id"]:
            found_list.append(note)
    return found_list


def find_notes_by_dates(date1, date2) -> list:
    notes_data = fw.read_csv()
    found_list = []
    for note in notes_data:
        date_note = datetime.datetime.strptime(note["date_note"], '%Y-%m-%d %H:%M:%S.%f')
        if (date1 < date_note < date2):
            found_list.append(note)
    return found_list
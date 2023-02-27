import view as view
import file_work as fw


def start_notes():
    while True:
        mode = view.get_mode()
        if mode == 1:
            view.put_message("\nВносим Записку:\n")
            data_new_note = view.get_add_new_note()
            fw.append_to_csv(fw.get_last_id(), data_new_note)
            view.put_message("Записка добавлена")

        elif mode == 2:
            view.put_message("\nВыводим список Записок:\n")
            data_notes = fw.read_csv_to_arr()
            view.print_to_screen(data_notes)

        elif mode == 3:
            view.put_message("\nИщем Записки по датам:")

        elif mode == 4:
            view.put_message("\nИщем Записку и выводим ее на экран:\n")
            find_note(view.input_message("Введите искомое"))

        elif mode == 5:
            view.put_message("Редактируем Записку:\n")

        elif mode == 6:
            view.put_message('Всего хорошего!\n')
            break
        print('\nДальше?\n')


def find_note(find_data):
    notes_data = fw.read_csv_to_arr()
    found_list = []
    for line in notes_data:
        if find_data in line:
            found_list.append(line)
    if found_list > []:
        for elem in found_list:
            print(elem, end='')
            print()
    else:
        print('Искомое не найдено')
    return

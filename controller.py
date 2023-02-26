import view as view
import file_work as fw

def start_notes():
    while True:
        mode = view.get_mode()
        if mode == 1:
            print("Вносим Записку:\n")
            data_new_note = view.get_add_new_note()
            fw.append_to_csv(fw.get_last_id(), data_new_note)

            
        elif mode == 2:
            print("Выводим список Записок:\n")


        elif mode == 3:
            print("Ищем Записки по датам:\n")
            
        elif mode == 4:
            print("Выводим Записку на экран:\n")
            
        elif mode == 5:
            print("Редактируем Записку:\n")
          
        elif mode == 6:
            print('Всего хорошего!\n')
            break             
        print('\nДальше?')
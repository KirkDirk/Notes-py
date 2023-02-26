import view as view
import file_work as fw

def start_notes():
    while True:
        mode = view.get_mode()
        if mode == 1:
            print("\nВносим Записку:")
            data_new_note = view.get_add_new_note()
            fw.append_to_csv(fw.get_last_id(), data_new_note)
           
        elif mode == 2:
            print("\nВыводим список Записок:")
            data_notes = fw.read_csv_to_arr()
            view.print_to_screen(data_notes) 

        elif mode == 3:
            print("\nИщем Записки по датам:")
            
        elif mode == 4:
            print("\nВыводим Записку на экран:")
            
        elif mode == 5:
            print("Редактируем Записку:\n")
          
        elif mode == 6:
            print('Всего хорошего!\n')
            break             
        print('\nДальше?\n')
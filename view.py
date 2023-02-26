import datetime

def get_mode() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие: ")
    print("1. Создать Записку")
    print("2. Вывести список всех Записок")
    print("3. Найти Записки по датам")
    print("4. Вывести Записку на экран")
    print("5. Редактировать записку")
    print("6. Закончить работу")
    print("=" * 20+ "\n")
    return int(input("Введите номер необходимого действия: "))

def get_search_key():
    print("\n" + "-" * 20)
    print("Выберите вид поиска: ")
    print("1. id")
    print("2. Фамилия")
    print("3. Имя")
    print("4. Должность")
    print("5. Телефон")
    print("-" * 20+ "\n")
    return int(input("Введите вид поиска: "))-1

def get_search_empl(data):
    search_data = input("Введите " + data + " сотрудника: ")
    return search_data

def print_to_console_found_empl(found_empl):
    if found_empl == None: 
        print("Данные не найдены")
    else:
        print(found_empl.values())

def get_search_by_position():
    search_position = input("Введите искомую должность: ")
    return search_position

def print_to_console_celection(found_list):
    if found_list == None: 
        print("Данные не найдены")
    else:
        for i in range(len(found_list)):
            print(found_list[i])
    
def get_search_by_salary():
    search_salary = input("Введите диапазон зарплат: ")
    return search_salary

def get_salary_range():
    hi_salary = input("Введите верхнюю границу: ")
    low_salary = input("Введите нижнюю границу: ")
    return [hi_salary, low_salary]

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
from data_functions import select_variant, read_data, write_data, change_entry, delete_entry, selection_data

def edit_data():
    filename = selection_data()

    data = read_data(filename)

    keyword = input("\nВведите имя или фамилию для изменения или удаления: ")

    print("\n Выберите действие (1 - изменить / 2 - удалить): \n")

    action = select_variant()
    if action == 1:
        change_entry(data, keyword)     # изменение данных
    elif action == 2:
        delete_entry(data, keyword)     # удаление данных
    else:
        print("Неверная команда.")

    write_data(filename, data)          # запись изменений


from data_create import name_data, surname_data, phone_data, address_data

def selection_data():           # Выбор какой файл редактировать
    print("В каком файле изменять данные? \n")
    var = select_variant()
    if var == 1:
        filename = 'data_first_variant.csv'
    elif var == 2:
        filename = 'data_second_variant.csv'
    return filename

def select_variant():           # выбор варианта
    var = int(input(f"Выберите вариант 1 или 2: "))
    while var != 1 and var != 2:
        print('Не правильный ввод!')
        var = int(input('Введите число "1" или "2": '))
    return var

def read_data(filename):         # чтение файла и запись в строку
    data = []
    if filename == 'data_first_variant.csv':
        with open(filename, 'r', encoding = 'utf-8') as file:
            record = []
            for line in file:
                line = line.strip()  
                if line:  
                    record.append(line)
                else: 
                    data.append(record)
                    record = []
            if record:
                data.append(record)
    elif filename == 'data_second_variant.csv':
        with open(filename, 'r', encoding = 'utf-8') as file:
            lines = file.readlines()
        data = [line.strip().split(';') for line in lines]
    return data

def write_data(filename, data):     # запись в файл
    if filename == 'data_first_variant.csv':
        with open(filename, 'w', encoding = 'utf-8') as file:
            for row in data:
                for item in row:
                    file.write(item + '\n')
                file.write('\n')  
    elif filename == 'data_second_variant.csv':    
        with open(filename, 'w', encoding = 'utf-8') as file:
            for row in data:
                file.write(';'.join(row) + '\n')


def find_entry(data, keyword):      # поиск нужной строки
    for i, row in enumerate(data):
        if keyword in row:
            return i
    return -1

def change_entry(data, keyword):        # запись обновлённой информации в файл
    index = find_entry(data, keyword)
    if index != -1:
        print(f"Найдена запись: {data[index]} \n")
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        new_data = [name,surname,phone,address]
        data[index] = new_data
        print("Запись успешно изменена.")
    else:
        print("Запись с указанными данными не найдена.")

def delete_entry(data, keyword):        # удаление из файла выбранной строки
    index = find_entry(data, keyword)
    if index != -1:
        print("Найдена запись для удаления:", data[index])
        print("Вы уверены, что хотите удалить эту запись? (1 - да / 2 - нет): ")
        confirmation = select_variant()
        if confirmation == 1:
            del data[index]
            print("Запись успешно удалена.")
    else:
        print("Запись с указанным ключевым словом не найдена.")

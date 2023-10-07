from data_create import family_data, surname_data, name_data,  phone_data

from os.path import exists

from csv import DictWriter, DictReader


def create_file():
    if not exists('Phone_book.csv'):
        with open('Phone_book.csv', "w", encoding="utf-8") as data:
            f_writer = DictWriter(data, fieldnames=['№', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
            f_writer.writeheader()
        lst = ['', '', '', '', '']
        write_file('Phone_book.csv', lst)
        with open('Phone_book.csv', encoding="utf-8") as data:
            f_reader = DictReader(data)
            result = list(f_reader)
            result.pop(0)
        with open('Phone_book.csv', "w", encoding="utf-8", newline='') as data:
            f_writer = DictWriter(data, fieldnames=['№', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
            f_writer.writeheader()
            f_writer.writerows(result)   


def get_info():
    with open('Phone_book.csv', encoding="utf-8") as data:
        f_reader = list(data)
        row_count = len(f_reader)
    number = f'{str(row_count)}: '
    family = family_data()
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    info = [number, family, name, surname, phone]
    return info


def show_contacts(file_name):
    print('Вот список Ваших контактов: \n')
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        result = list(f_reader)
        for row in result:
            print(row['№'], row['Фамилия'], row['Имя'], row['Отчество'], row['Номер телефона'])

    return result


def write_file(file_name, lst):
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        result = list(f_reader)
    obj = {'№': lst[0], 'Фамилия': lst[1], 'Имя': lst[2], 'Отчество': lst[3], 'Номер телефона': lst[4]}
    result.append(obj)
    with open('Phone_book.csv', "w", encoding="utf-8", newline='') as data:
        f_writer = DictWriter(data, fieldnames=['№', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
        f_writer.writeheader()
        f_writer.writerows(result)


def change_contact(file_name):
    row_to_change = int(input('Введите номер записи для изменения: ')) - 1
    changed_row = get_info()
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        result = list(f_reader)
    obj = {'№': str(row_to_change + 1), 'Фамилия': changed_row[1], 'Имя': changed_row[2], 'Отчество': changed_row[3], 'Номер телефона': changed_row[4]}
    result[row_to_change] = obj
    with open('Phone_book.csv', "w", encoding="utf-8", newline='') as data:
        f_writer = DictWriter(data, fieldnames=['№', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
        f_writer.writeheader()
        f_writer.writerows(result)


def delete_contact(file_name):
    row_to_delete = int(int(input('Введите номер записи для удаления: ')) - 1)
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        result = list(f_reader)
        result.pop(row_to_delete)
        number_contact = 1
        for row in result:
            row['№'] = number_contact
            number_contact += 1
    with open('Phone_book.csv', "w", encoding="utf-8", newline='') as data:
        f_writer = DictWriter(data, fieldnames=['№', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
        f_writer.writeheader()
        f_writer.writerows(result)   
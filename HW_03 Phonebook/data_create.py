def family_data():
    name = input('Введите фамилию: ')
    return name


def name_data():
    name = input('Введите имя: ')
    return name


def surname_data():
    surname = input('Введите отчество: ')
    return surname


def phone_data():
    phone = input('Введите Ваш телефон: ')
    return phone

# with open('Phone_book.csv', encoding="utf-8") as data:
#     f_reader = list(data)
#     row_count = len(f_reader) 
#     print(row_count)
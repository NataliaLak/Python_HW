from scripts import create_file, show_contacts, write_file, get_info, change_contact, delete_contact




def interface():
    create_file()

    print('\nДобро пожаловать в телефонную книгу!\n\n'
          'Вы можете:')
    
    while True:
        print('\n1 - Показать список контактов\n'
              '2 - Записать контакт\n'
              '3 - Изменить контакт\n'
              '4 - Удалить контакт\n'
              '5 - выйти из программы\n')  
        try:
            command = int(input('Введите команду: ')) 
        except ValueError:
            command = -1

        while command < 1 or command > 6:
            print('\nВы ввели неверный номер команды!\n')
            try:
                command = int(input('Введите команду: ')) 
            except ValueError:
                command = -1

        if command == 1:
            show_contacts('Phone_book.csv')
        elif command == 2:
            write_file('Phone_book.csv', get_info())
        elif command == 3:
            change_contact('Phone_book.csv')
        elif command == 4:
            delete_contact('Phone_book.csv')
        elif command == 5:
            print('Спасибо, что воспользовались нашей программой!')
            break
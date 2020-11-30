users = []
books = []
dictionary = []


def readers_search():
    user_name = input('Введите имя читателя: ')
    user_lastname = input('Введите фамилию читателя: ')
    for i in users:
        if i['name'] == user_name and i['lastname'] == user_lastname:
            text = f'''Читатель найден:
Имя: {i['name']}
Фамилия: {i['lastname']}
Номер телефона: {i['phone']}
Адрес: {i['address']}
Должник: {'да' if i['name'] in output_readers() else 'нет'}
'''
            return text
    return f'Читатель {user_name} {user_lastname} не найден'


def book_search():
    book_name = input('Введите название книги: ')
    book_author = input('Введите автора книги: ')
    for i in books:
        if i['name'] == book_name and i['author'] == book_author:
            text = f'''Книга найдена:
Название: {i['name']}
Автор: {i['author']}
Год создания: {i['date']}
Количество: {i['count']}
'''
            return text
    return f'Книга {book_name} автора {book_author} не найдена'


def new_reader():
    user_name = input('Введите имя нового читателя: ')
    user_lastname = input('Введите фамилию нового читателя: ')
    user_phone = input('Введите номер нового читателя: ')
    user_address = input('Введите адрес нового читателя: ')
    user = (user_name, user_lastname)
    if user not in [(i['name'], i['lastname']) for i in users]:
        user_dict = {'name': user_name,
                     'lastname': user_lastname,
                     'phone': user_phone,
                     'address': user_address}
        users.append(user_dict)
        return f'Читатель {user_name} {user_lastname} успешно зарегистрирован'
    else:
        return 'Такой пользователь уже существует'


def new_book():
    book_name = input('Введите название новой книги: ')
    book_author = input('Введите автора книги: ')
    book_found = input('Введите год создания книги: ')
    if book_name in [i['name'] for i in books]:
        if book_author in [i['author'] for i in books]:
            for i in books:
                if i['name'] == book_name:
                    i['count'] = i['count'] + 1
    else:
        book_dict = {'name': book_name,
                     'author': book_author,
                     'date': book_found,
                     'count': 1}
        books.append(book_dict)
    return f'Книга {book_name} автора {book_author} успешно добавлена'


def get_book():
    user_name = input('Введите имя читателя: ')
    user_lastname = input('Введите фамилию читателя: ')
    user = (user_name, user_lastname)
    if user in [(i['name'], i['lastname']) for i in users]:
        book_name = input('Введите название книги: ')
        book_author = input('Введите автора книги: ')
        book = (book_name, book_author)
        if book in [(i['name'], i['author']) for i in books]:
            dictionary.append([*user, *book])
            print(dictionary)
            for i in books:
                if i['name'] == book_name and i['author'] == book_author:
                    if i['count'] != 0:
                        i['count'] = i['count'] - 1
                    else:
                        return 'Не хватает книг'
            return f'Читатель {user_name} взял книгу {book_name}'
        else:
            return 'Такой книги нет в базе'
    else:
        return 'Такого читателя нет в базе'


def return_book():
    user_name = input('Введите имя читателя: ')
    user_lastname = input('Введите фамилию читателя: ')
    book_name = input('Введите название книги: ')
    book_author = input('Введите автора книги: ')
    counter = 0
    for i in dictionary:
        if i[0] == user_name and i[1] == user_lastname and i[2] == book_name and i[3] == book_author:
            del dictionary[counter]
            for j in books:
                if j['name'] == book_name:
                    j['count'] = j['count'] + 1
            return f'Читатель {user_name} отдал книгу {book_name}'
        counter += 1
    return 'Неверно указан имя читателя или название книги'


def output_readers():
    users_output = []
    for i in dictionary:
        users_output.append(i[0])
    users_output = list(set(users_output))
    return users_output


while True:
    print(' ')
    print('1. Создание читателя')
    print('2. Создание новой книги')
    print('3. Поиск читателя')
    print('4. Поиск книги')
    print('5. Выдача книги')
    print('6. Прием книги обратно')
    print('7. Вывод должников')
    print('8. Выход\n')

    try:
        user_choice = int(input('Введите команду: '))

        if user_choice == 3:
            print(readers_search())
        elif user_choice == 4:
            print(book_search())
        elif user_choice == 1:
            print(new_reader())
        elif user_choice == 2:
            print(new_book())
        elif user_choice == 5:
            print(get_book())
        elif user_choice == 6:
            print(return_book())
        elif user_choice == 7:
            print(output_readers())
        elif user_choice == 8:
            break
    except ValueError:
        print('Мне нужен выбор (цифрой)')

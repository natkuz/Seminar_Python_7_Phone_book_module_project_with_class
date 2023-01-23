import controller

commands = [
    'Открыть файл',
    'Сохранить файл',
    'Показать все контакты',
    'Создать контакт',
    'Удалить контакт',
    'Изменить контакт',
    'Найти контакт',
    'Выход из программы'
]


def main_menu() -> int:
    print('\nГлавное меню:')
    for i, line in enumerate(commands, 1):
        print(f'\t{i}. {line}')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 9:
                return choice
            else:
                print('\nТакого пункта нет. Попытайтесь еще раз.')
        except ValueError:
            print('\nВведено неверное значение. Попробуйте еще раз. ')


def input_error():
    print('\nОшибка ввода. Нет такого номера.')


def exit_prog():
    print('\nПрограмма завершена. До свидания!')


def view_open_file():
    print('\nФайл успешно открыт. Что дальше?')


def show_contacts(phone_list: list):
    print('\nТелефонная книга:')
    if len(phone_list) < 1:
        print('\tТелефонная книга пуста или не открыта')
    else:
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')


def create_new_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment


def modification_contact():
    print('Введите новые данные. Если изменения не требуются, нажмите Enter')
    name = input('Введите новое имя и фамилию: ')
    phone = input('Введите новый номер телефона: ')
    comment = input('Введите новый комментарий: ')
    return name, phone, comment


def select_change_contact():
    while True:
        try:
            contact_for_change = int(input('\nВыберите номер контакта, который хотите изменить: '))
            return contact_for_change
        except ValueError:
            print('\nЧислом, пожалуйста. Попробуйте еще раз. ')


def find_contact():
    find = input('\nЧто ищем? ')
    return find


def save_phone_book():
    print('\nТелефонная книга сохранена')


def del_contact():
    while True:
        try:
            contact_for_delete = int(input('\nВыберите номер контакта, который хотите удалить: '))
            return contact_for_delete
        except ValueError:
            print('\nЧислом, пожалуйста. Попробуйте еще раз. ')


def del_confirm(contact: int, name: str):
    if contact:
        result = input(f'Вы действительно хотите удалить контакт "{name}"? (y/n): ').lower()
        if result == 'y':
            return True
        else:
            return False


def view_changes():
    print('\nИзменения внесены, осталось сохранить.')


def undo_changes():
    print('\nИзменения отменены. Возвращаемся в главное меню')


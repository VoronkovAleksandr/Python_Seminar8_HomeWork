# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска о
#    определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# ДЗ
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных


def read_data(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        data = list(map(lambda x: x.replace('\n', ''), data))
        return data
def input_data():
    data = input('Введите Фамилию Имя Отчечство: ') + ' | '
    data += input('Введите номер телефона: ')
    return data

def add_data(file, data):
    with open(file, 'a', encoding='utf-8') as f:
        f.write('\n' + data)

def write_data(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(data)

def find_data(text) -> int:
    data = read_data('data.txt')
    result = [x for x in data if text in x]
    if len(set(result)) == 1:
        result = str(*result)
        print(f'\nНашёл: {result} \n')
        return data.index(result)
    elif len(set(result)) >1:
        print('\nТаких записей много, уточните поиск\n')
        print_data(result)
    else:
        print("\nНе нашел :(\n")

def print_data(data):
    print('\n'.join(data))

def del_data(index):
    if index:
        data = read_data('data.txt')
        print('Введите новые данные')
        if input('Введите 1 для подтверждения удаления: ') == '1': 
            data.pop(index)
            to_write = '\n'.join(data)
            write_data('data.txt', to_write)
            print('Данные удалил')
        else:
            print('Не подтверждено')

def edit_data(index):
    if index:
        data = read_data('data.txt')
        data[index] = input_data()
        to_write = '\n'.join(data)
        write_data('data.txt', to_write)
        print('Данные заменил')

while True:
    choice = input('\n   Прочитать данные - r \
                   \n   Ввести данные - w \
                   \n   Найти данные - f \
                   \n   Изменить данные - e \
                   \n   Удалить данные - d \
                   \n   Выйти - 0 \
                   \n   Выберите что надо сделать: ')
    if choice == 'r': print_data(read_data('data.txt'))
    elif choice == 'w': add_data('data.txt' ,input_data())
    elif choice == 'f': index = find_data(input('Введите данные для поиска: '))
    elif choice == 'd': del_data(find_data(input('Введите данные для поиска: ')))
    elif choice == 'e': edit_data(find_data(input('Введите данные для поиска: ')))
    elif choice == '0': 
        print('Пока!')
        break
    else: print('Ошибка, повторите выбор: ')

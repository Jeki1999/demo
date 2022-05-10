documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people():
    number = input('Введите номер документа: ')
    for document in documents:
        if document['number'] == number:
            print(document["name"])


def shelf():
    number = input('Введите номер документа: ')
    for id, directory in directories.items():
        if number in directory:
            print(id)


def list():
  for list in documents:
    type = list['type']
    number = list['number']
    name = list['name']
    print(f' {type} "{number}" "{name}";')


def add():
    document_type = input('Введите тип документа: ')
    document_number = input('Введите номер документа: ')
    document_name = input('Введите имя владельца документа: ')
    shelf_number = input('Введит номер полки: ')
    if shelf_number not in directories:
      print('Такой полки нет')
    new_document = dict(type = document_type, number = document_number, name = document_name)
    documents.append(new_document)
    directories[shelf_number] += [document_number]
    print('Документ добавлен')


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            people()
        elif command == 's':
            shelf()
        elif command == 'l':
            list()
        elif command == 'a':
            add()
        elif command == 'q':
            print('Выход')
            break


main()
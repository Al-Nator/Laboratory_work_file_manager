from file_manager import FileManager

def print_menu():
    print("Файловый менеджер - Команды:")
    print("1 - Показать содержимое текущей директории")
    print("2 - Создать директорию")
    print("3 - Удалить директорию")
    print("4 - Перейти в директорию")
    print("5 - Вернуться в директорию выше")
    print("6 - Создать файл")
    print("7 - Читать файл")
    print("8 - Записать в файл")
    print("9 - Удалить файл")
    print("10 - Копировать файл")
    print("11 - Переместить файл")
    print("12 - Переименовать файл")
    print("0 - Выход")
    print()

def main():
    manager = FileManager()
    while True:
        print_menu()
        command = input("Введите номер команды: ")
        if command == '0':
            break
        elif command == '1':
            print(manager.list_directory())
        elif command == '2':
            dir_name = input("Введите имя новой директории: ")
            manager.create_directory(dir_name)
        elif command == '3':
            dir_name = input("Введите имя удаляемой директории: ")
            manager.delete_directory(dir_name)
        elif command == '4':
            dir_name = input("Введите имя директории для перехода: ")
            manager.change_directory(dir_name)
        elif command == '5':
            manager.go_up()
        elif command == '6':
            file_name = input("Введите имя создаваемого файла: ")
            manager.create_file(file_name)
        elif command == '7':
            file_name = input("Введите имя файла для чтения: ")
            print(manager.read_file(file_name))
        elif command == '8':
            file_name = input("Введите имя файла для записи: ")
            content = input("Введите содержимое файла: ")
            manager.write_file(file_name, content)
        elif command == '9':
            file_name = input("Введите имя удаляемого файла: ")
            manager.delete_file(file_name)
        elif command == '10':
            source = input("Введите имя копируемого файла: ")
            destination = input("Введите имя нового файла: ")
            manager.copy_file(source, destination)
        elif command == '11':
            source = input("Введите имя перемещаемого файла: ")
            destination = input("Введите новое место назначения файла: ")
            manager.move_file(source, destination)
        elif command == '12':
            old_name = input("Введите текущее имя файла: ")
            new_name = input("Введите новое имя файла: ")
            manager.rename_file(old_name, new_name)
        else:
            print("Неверная команда, попробуйте ещё раз.")

if __name__ == '__main__':
    main()

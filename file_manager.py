import os
import shutil
from config import WORKING_DIRECTORY

class FileManager:
    def __init__(self):
        self.current_directory = WORKING_DIRECTORY

    def list_directory(self):
        try:
            return os.listdir(self.current_directory)
        except FileNotFoundError:
            print(f"Директория '{self.current_directory}' не найдена.")
        except Exception as e:
            print(f"Произошла ошибка при попытке просмотреть директорию: {e}")

    def create_directory(self, dir_name):
        try:
            os.mkdir(os.path.join(self.current_directory, dir_name))
        except FileExistsError:
            print(f"Директория '{dir_name}' уже существует.")
        except Exception as e:
            print(f"Произошла ошибка при создании директории '{dir_name}': {e}")

    def delete_directory(self, dir_name):
        try:
            os.rmdir(os.path.join(self.current_directory, dir_name))
        except FileNotFoundError:
            print(f"Директория '{dir_name}' не найдена для удаления.")
        except Exception as e:
            print(f"Произошла ошибка при удалении директории '{dir_name}': {e}")

    def change_directory(self, dir_name):
        try:
            new_dir = os.path.join(self.current_directory, dir_name)
            if os.path.commonprefix([WORKING_DIRECTORY, new_dir]) == WORKING_DIRECTORY:
                self.current_directory = new_dir
            else:
                print("Действие запрещено: выход за пределы рабочей директории.")
        except FileNotFoundError:
            print(f"Директория '{dir_name}' не найдена.")
        except Exception as e:
            print(f"Произошла ошибка при смене директории на '{dir_name}': {e}")
            
    def go_up(self):
        try:
            parent_directory = os.path.dirname(self.current_directory)
            if os.path.commonprefix([WORKING_DIRECTORY, parent_directory]) == WORKING_DIRECTORY:
                self.current_directory = parent_directory
            else:
                print("Действие запрещено: выход за пределы рабочей директории.")
        except FileNotFoundError:
            print(f"Родительская директория не найдена.")
        except Exception as e:
            print(f"Произошла ошибка при попытке подняться на уровень выше: {e}")

    def create_file(self, file_name):
        try:
            with open(os.path.join(self.current_directory, file_name), 'w') as file:
                file.write('')
        except Exception as e:
            print(f"Произошла ошибка при создании файла '{file_name}': {e}")

    def read_file(self, file_name):
        try:
            with open(os.path.join(self.current_directory, file_name), 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")
        except Exception as e:
            print(f"Произошла ошибка при чтении файла '{file_name}': {e}")

    def write_file(self, file_name, content):
        try:
            with open(os.path.join(self.current_directory, file_name), 'w') as file:
                file.write(content)
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден для записи.")
        except Exception as e:
            print(f"Произошла ошибка при записи в файл '{file_name}': {e}")

    def delete_file(self, file_name):
        try:
            os.remove(os.path.join(self.current_directory, file_name))
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден для удаления.")
        except Exception as e:
            print(f"Произошла ошибка при удалении файла '{file_name}': {e}")

    def copy_file(self, source, destination):
        try:
            shutil.copy(os.path.join(self.current_directory, source),
                        os.path.join(self.current_directory, destination))
        except FileNotFoundError:
            print(f"Исходный файл '{source}' не найден для копирования.")
        except Exception as e:
            print(f"Произошла ошибка при копировании файла '{source}': {e}")

    def move_file(self, source, destination):
        try:
            shutil.move(os.path.join(self.current_directory, source),
                        os.path.join(self.current_directory, destination))
        except FileNotFoundError:
            print(f"Исходный файл '{source}' не найден для перемещения.")
        except Exception as e:
            print(f"Произошла ошибка при перемещении файла '{source}': {e}")

    def rename_file(self, old_name, new_name):
        try:
            os.rename(os.path.join(self.current_directory, old_name),
                      os.path.join(self.current_directory, new_name))
        except FileNotFoundError:
            print(f"Файл '{old_name}' не найден для переименования.")
        except Exception as e:
            print(f"Произошла ошибка при переименовании файла '{old_name}': {e}")

    

if __name__ == '__main__':
    manager = FileManager()

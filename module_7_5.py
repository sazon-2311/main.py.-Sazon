from os import walk, getcwd
from os.path import getmtime, getsize, dirname
from time import strftime, localtime


def file_info(directory):
    for root, dirs, files in walk(directory):
        for file in files:
            filepath = getcwd()
            filetime = getmtime(filepath)
            formatted_time = strftime("%d.%m.%Y %H:%M", localtime(filetime))
            filesize = getsize(file)
            parent_dir = dirname(filepath)
            print(f'Обнаружен файл: {file},',
                  f'Путь: {filepath},',
                  f'Размер: {filesize} байт,',
                  f'Время изменения: {formatted_time},',
                  f'Родительская директория: {parent_dir}')


if __name__ == '__main__':
    file_info('.')

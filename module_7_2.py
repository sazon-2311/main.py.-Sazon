def custom_write(file_name: str, strings: list):
    strings_positions = {}
    line_number = 1
    file = open(file_name, 'w')
    for i in strings:
        start_byte = file.tell()
        file.write(f'{i}\n')
        strings_positions[(line_number, start_byte)] = i
        line_number += 1
    file.close()
    return strings_positions


if 1 > 0:
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

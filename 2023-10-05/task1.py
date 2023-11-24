# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени
# добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только
# для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
# берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное
# имя, если оно передано. Далее счётчик файлов и расширение. 3.Соберите из созданных на
# уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os

path = os.path.join('.', 'for_rename')

def mass_rename(path, new_name, digits_num=1, source_ext=None, dest_ext=None,\
                saved_name_range=None):
    os.chdir(path)
    file_num = 1
    saved_name_range_start, saved_name_range_last = saved_name_range
    for f in os.listdir():
        dest_name = new_name + ('0' * (digits_num - 1)) + str(file_num)
        ext = os.path.splitext(f)[1]
        if source_ext and ext != source_ext:
            continue
        if dest_ext:
            dest_name += dest_ext
        else:
            dest_name += ext
        if saved_name_range:
            dest_name = f[saved_name_range_start:saved_name_range_last] + dest_name
        os.rename(f, dest_name)
        file_num += 1

params = {
    'new_name': 'file',
    'digits_num': 2,
    'source_ext': '.txt',
    'dest_ext': '.txt1',
    'saved_name_range': [1,3]
}

mass_rename(path, **params)
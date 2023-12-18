# 2. Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих
# файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним
# прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

from pathlib import Path


def rename_files(dir_in: str, wish_file_name: str, num_digits: int, extension_name_in: str, extension_name_out: str,
                 char_range: list[int]):
    # входная директория с файлами
    path_in = Path(dir_in)

    # получаем список файлов и подпапок в основной директории
    entities_gen = (p for p in path_in.rglob("*"))

    # формируем начальное порядковое число
    start_count = int('1' + '0' * (num_digits - 1))
    print(start_count)

    # переименование файлов в папке и подпапках
    for entity in entities_gen:
        if entity.is_file():
            if entity.suffix[1:].lower() == extension_name_in.lower():
                new_name = (f'{entity.stem[char_range[0]:char_range[1] + 1] + wish_file_name + str(start_count)+'.'}'
                            f'{extension_name_out}')
                start_count += 1
                Path(entity).rename(Path(entity).parents[0] / new_name)


if __name__ == '__main__':
    rename_files('D:\\29. Погружение в Python. Часть 1 (семинары)\\07\\RENAME_Dir', 'renamed',
                 6, 'txt', 'aka', [3, 6])

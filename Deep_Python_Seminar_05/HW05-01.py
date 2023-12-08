# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Как пример
# C:\Windows\System32\hvsievaluator.exe

sys_path_text = 'C:/Windows/System32/hvsievaluator.exe'


def tuple_of_elements(absolute_path: str) -> tuple[str, str, str]:
    tuple_first_el = '/'.join(sys_path_text.split('/')[:-1]) + '/'
    tuple_second_el = ''.join(sys_path_text.split('/')[-1].split('.')[:-1])
    tuple_third_el = sys_path_text.split('/')[-1].split('.')[-1]
    return tuple_first_el, tuple_second_el, tuple_third_el


print(tuple_of_elements(sys_path_text))

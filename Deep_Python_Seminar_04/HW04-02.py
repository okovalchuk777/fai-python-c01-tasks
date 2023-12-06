# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.
import typing


def dict_func(**kwargs) -> dict:
    new_dict = {}
    for key, value in kwargs.items():
        if isinstance(value,typing.Hashable):
            new_dict[value] = key
        else:
            new_dict[str(value)] = key
    return new_dict

print(dict_func(first=13,second=15,third=25,forth=30))
print(dict_func(first=13,second=[],third=25,forth=30))
print(dict_func(first=13,second=15,third={},forth=(1,)))
print(dict_func(first=13,second='abcd',third={1,2,},forth=(1,)))

def func_add_nums(init_num):
    """
    На вход функции подаётся список чисел и символов. Функция выводит сумму чисел.
    При вводе символа q выполнение программы завершается.

    Позиционный параметр:
    init_num - список чисел и символов.

    help(func_add_nums)
    """
    sum_result = 0
    while 'q' not in init_num:
        for i in init_num:
            if i.isdecimal():
                sum_result += int(i)
        print(sum_result)
        init_num = input("Enter a string of multiple numbers separated by spaces: ").split()
    else:
        for i in init_num:
            if i.isdecimal():
                sum_result += int(i)
    return print(sum_result)


init_nums = input("Enter a string of multiple numbers separated by spaces: ").split()

func_add_nums(init_nums)

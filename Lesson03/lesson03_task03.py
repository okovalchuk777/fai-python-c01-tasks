def func_add_largest_args(a, b, c):
    if a < b and a < c:
        return print(f"{b + c:.7f}")
    elif b < a and b < c:
        return print(f"{a + c:.7f}")
    elif c < a and c < b:
        return print(f"{a + b:.7f}")
    else:
        return print("Числа не должны совпадать.")


arg01 = float(input("Введите первое число: "))
arg02 = float(input("Введите второе число: "))
arg03 = float(input("Введите третье число: "))
func_add_largest_args(arg03, arg02, arg01)

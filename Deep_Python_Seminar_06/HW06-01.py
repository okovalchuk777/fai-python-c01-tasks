# 2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from sys import argv


def _is_not_leap(year: int) -> bool:
    return not (year % 400 == 0 or year % 100 != 0 and year % 4 == 0)


def check_date(full_date: str) -> bool:
    day, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    elif month == 2 and day > 29:
        return False
    elif month == 2 and day > 28 and _is_not_leap(year):
        return False
    else:
        return True


if __name__ == '__main__':
    print(check_date(argv[1]))
    # print(check_date('29.02.2024'))
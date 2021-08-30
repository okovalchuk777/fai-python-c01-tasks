"""
How to concatenate items in a list to a single string?
https://stackoverflow.com/questions/12453580/how-to-concatenate-items-in-a-list-to-a-single-string
"""

init_number = int(input("Enter a number: "))


def fact_range(n):
    for i in range(1, n + 1):
        yield i


def fact_calculate(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
        i += 1
    return result


# f = fact_range(init_number)
# print(f)

list01 = [el for el in fact_range(init_number)]
str01 = " * ".join(map(str, list01))
print(f'{init_number}! = {str01} = {fact_calculate(init_number)}')

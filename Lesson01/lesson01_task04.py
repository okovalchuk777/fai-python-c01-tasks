'''
Useful link
https://studassistent.ru/pascal/nayti-samuyu-bolshuyu-cifru-celogo-polozhitelnogo-chisla-pascal-1
'''
n = int(input("Enter a number: "))
i_set = 0
while n > 0:
    i_init = n % 10  # Остаток от деления
    n = n // 10  # Целочисленное деление
    if i_init > i_set:
        i_set = i_init
print(i_set)

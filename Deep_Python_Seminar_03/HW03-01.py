# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

main_list = [2, 4, 4, 6, 6, 7, 15, 14, 14, 4, 17, 6, 29]
duplicate_list = []
unique_list = []

for i in main_list:
    if i not in unique_list:
        unique_list.append(i)
    else:
        duplicate_list.append(i)

print(f'Начальный список {main_list}')
print(f'Список из дублирующихся элементов {duplicate_list}')
print(f'Список из уникальных элементов {unique_list}')
        
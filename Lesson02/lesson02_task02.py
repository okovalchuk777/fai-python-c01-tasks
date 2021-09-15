init_list = str(input("Enter a sequence of values through a space (number, string, boolean, None etc.): ")).split()
final_list = []
i = 0
for el in init_list[::2]:
    if i < len(init_list) - 1:
        final_list.append(init_list[i + 1])
    final_list.append(el)
    i += 2

print(final_list)

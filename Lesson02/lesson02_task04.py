init_string = str(input("Enter a string of multiple words separated by spaces: ")).split()
for ind, el in enumerate(init_string, 1):
    print(ind, el[:10])

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# переменные, принимающие значения 1 и 0
# http://mtcol.ru/elt/logics/project/p1aa1.html
# https://blog.finxter.com/python-bitwise-not-operator/
# Swapping 1 with 0 and 0 with 1 in a Pythonic way
# https://stackoverflow.com/questions/1779286/swapping-1-with-0-and-0-with-1-in-a-pythonic-way

values_count = 2  # 0, 1
variables_count = 3  # x, y, z
count = 0
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            #print(x, y, z)
            predicate = (1 - (x or y or z)) == ((1 - x) and (1 - y) and (1 - z))
            print(bool(predicate))
            if bool(predicate):
                count += 1
#print(count)
if count == values_count ** variables_count:
    print("Предикат верен!")
else:
    print("Предикат НЕверен!")

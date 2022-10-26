# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Run-length encoding (RLE)
# Consider a screen containing plain black text on a solid white background. There will be many long runs of  white
# pixels in the blank space, and many short runs of black pixels within the text. A hypothetical scan line,
# with B  representing a black pixel and W representing white, might read as follows:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# With a run-length encoding (RLE) data compression algorithm applied to the above hypothetical scan line,
# it can  be rendered as follows:
# 12W1B12W3B24W1B14W
# https://en.wikipedia.org/wiki/Run-length_encoding

# функция считывания из файлов первой строки
def first_line_of_file_to_val(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        return lines[0]


text01 = first_line_of_file_to_val('input.txt')

print(text01)
text02 = text01[:]
zip_text = ''

count = 0

text02_len = len(text02) - 1
for index, x in enumerate(text02):
    if (index + 1) != text02_len and text02[index] == text02[index + 1]:
        count += 1
    elif (index + 1) != text02_len and text02[index] != text02[index + 1]:
        count += 1
        zip_text = zip_text + str(count) + text02[index]
        count = 0
    elif (index + 1) == text02_len:
        count += 1
        if text02[index] == text02[index + 1]:
            count += 1
            zip_text = zip_text + str(count) + text02[index]
            count = 0
            break
        elif text02[index] != text02[index + 1]:
            zip_text = zip_text + str(count) + text02[index] + '1' + text02[index + 1]
            count = 0
            break

print(zip_text)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(zip_text)

# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

search_string = 'абв'
text = 'абвер яблоко ананас Зимбабве забвение селёдка редиска абвгдейка'
print(text)

list01 = text.split()
# print(list01)
list02 = [i for i in list01 if i.find(search_string) == - 1]
print(' '.join(list02))

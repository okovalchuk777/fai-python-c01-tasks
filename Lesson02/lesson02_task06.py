'''
Как получить позицию элемента из вложенного списка в python
https://coderoad.ru/63636591/%D0%9A%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C
-%D0%BF%D0%BE%D0%B7%D0%B8%D1%86%D0%B8%D1%8E-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%B0-%D0%B8%D0%B7-
%D0%B2%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B0-%D0%B2-python
list01[0][1]['название']
list01[0][1]['цена']
list01[0][1]['количество']
list01[0][1]['ед']
Как вывести значение словаря, преобразовав его из списка в строку?
https://ru.stackoverflow.com/questions/507024/%d0%9a%d0%b0%d0%ba-%d0%b2%d1%8b%d0%b2%d0%b5%d1%81%d1%82%d0%b8-
%d0%b7%d0%bd%d0%b0%d1%87%d0%b5%d0%bd%d0%b8%d0%b5-%d1%81%d0%bb%d0%be%d0%b2%d0%b0%d1%80%d1%8f-
%d0%bf%d1%80%d0%b5%d0%be%d0%b1%d1%80%d0%b0%d0%b7%d0%be%d0%b2%d0%b0%d0%b2-%d0%b5%d0%b3%d0%be-%d0%b8%d0%b7-
%d1%81%d0%bf%d0%b8%d1%81%d0%ba%d0%b0-%d0%b2-%d1%81%d1%82%d1%80%d0%be%d0%ba%d1%83
for key, value in product_analytics_dict.items():
    print(key, ':', ', '.join(str(num) for num in value), sep='')
'''

offer = input("Вы готовы внести информацию о товарах? Ввведите да или нет: ")
goods_list = []
i = 0
while offer == 'да':
    i += 1
    name = input("Введите название товара: ")
    price = int(input("Введите стоимость: "))
    quantity = int(input("Введите количество: "))
    measure = input("Введите единицы измерения: ")
    goods_tuple = (i, {'название': name, 'цена': price, 'количество': quantity, 'ед': measure})
    goods_list.append(goods_tuple)
    offer = input("Информация сохранена. Вы готовы внести информацию о следующем товаре? Ввведите да или нет: ")
print(goods_list)

# goods_list = [(1, {'название': 'пк', 'цена': 3, 'количество': 4, 'ед': 'ш'}), (2, {'название': 'принтер', 'цена': 5, 'количество': 6, 'ед': 'ш'})]
name_list = []
for i in range(len(goods_list)):
    el = goods_list[i][1]['название']
    if el not in name_list:
        name_list.append(el)
#print(name_list)
price_list = []
for i in range(len(goods_list)):
    el = goods_list[i][1]['цена']
    if el not in price_list:
        price_list.append(el)
#print(price_list)
quantity_list = []
for i in range(len(goods_list)):
    el = goods_list[i][1]['количество']
    if el not in quantity_list:
        quantity_list.append(el)
#print(quantity_list)
measure_list = []
for i in range(len(goods_list)):
    el = goods_list[i][1]['ед']
    if el not in measure_list:
        measure_list.append(el)
#print(measure_list)

product_analytics_dict = {'название': name_list, 'цена': price_list, 'количество': quantity_list, 'ед': measure_list}
print(f'Аналитика товаров представлена ниже \n {product_analytics_dict}')


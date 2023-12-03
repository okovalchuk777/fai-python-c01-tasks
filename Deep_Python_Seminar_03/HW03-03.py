# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

from itertools import permutations

BACKPACK_WEIGHT = 25000
VARIANTS = 100000

# вес дан в граммах
things_dict = {'палатка': 1100,
               'спальник': 700,
               'газовая горелка': 1500,
               'газовый балон 1': 450,
               'газовый балон 2': 450,
               'зарядное устройство': 392,
               'кружка': 60,
               'ложка': 18,
               'тарелка': 154,
               'нож': 270,
               'котелок': 480,
               'фонарик': 250,
               'бутылка воды 1': 2000,
               'бутылка воды 2': 2000,
               'бутылка воды 3': 2000,
               'аптечка': 1000,
               'средства личной гигиены': 1000,
               'паек 1': 1625,
               'паек 2': 1625,
               'паек 3': 1625,
               'паек 4': 1625,
               'паек 5': 1625,
               'паек 6': 1625,
               'консерва 1': 340,
               'консерва 2': 340,
               'консерва 3': 340,
               'чай': 50,
               'зажигалка': 57,
               'топорик': 1500,
               'другое': 1000}

keys_things_dict = [key for key in things_dict.keys()]

count = 1
best_weight = 0
best_things_dict = {}
for item_variant in permutations(things_dict.keys()):
    if count < VARIANTS:
        count += 1
        new_things_dict01 = {key1: things_dict[key1] for key1 in item_variant}
        weight = 2000
        new_things_dict02 = {}
        for key2, value2 in new_things_dict01.items():
            if weight + value2 < BACKPACK_WEIGHT:
                weight += value2
                new_things_dict02[key2] = value2
        print(new_things_dict02)
        print(weight)
        if weight > best_weight:
            best_weight = weight
            best_things_dict = new_things_dict02
    else:
        break
print(count)
print(best_weight)
print(best_things_dict)

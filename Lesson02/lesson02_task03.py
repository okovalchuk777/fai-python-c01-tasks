month = int(input("Enter the month as an integer from 1 to 12: "))
winter_list = [1, 2, 12]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
fall_list = [9, 10, 11]
if month in winter_list:
    print(f'This month refers to winter.')
elif month in spring_list:
    print(f'This month refers to spring.')
elif month in summer_list:
    print(f'This month refers to summer.')
elif month in fall_list:
    print(f'This month refers to fall.')

season_dict = {
    '1': 'winter',
    '2': 'winter',
    '3': 'spring',
    '4': 'spring',
    '5': 'spring',
    '6': 'summer',
    '7': 'summer',
    '8': 'summer',
    '9': 'fall',
    '10': 'fall',
    '11': 'fall',
    '12': 'winter'
}
print(f'This month refers to {season_dict.get(str(month))}.')

rating_element = int(input("Enter a new rating element: "))
my_list = [25, 18, 17, 17, 7, 7, 5, 3, 3, 2]
if rating_element > max(my_list):
    my_list.insert(0, rating_element)
elif rating_element < min(my_list):
    my_list.append(rating_element)
elif rating_element in my_list:
    index = my_list[::-1].index(rating_element)
    if index != 0:
        my_list.insert(-index, rating_element)
    else:
        my_list.insert(-1, rating_element)
elif rating_element not in my_list and min(my_list) < rating_element < max(my_list):
    for el in my_list[::-1]:
        if el > rating_element:
            index = my_list[::-1].index(el)
            my_list.insert(-index, rating_element)
            break
print(my_list)

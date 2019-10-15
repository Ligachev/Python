def find_small(list):
    '''Функция выбора наименьшего значения из списка'''
    small = list[0]
    small_index = 0
    for i in range (1, len(list)):
        if list[i] < small:
            small = list[i]
            small_index = i
    return small_index

def selectinon_sort(list):
    '''Функция сортировки списка'''
    new_list = []
    for i in range(len(list)):
        small = find_small(list)
        new_list.append(list.pop(small))
    return new_list

import random
rand = []
for i in range(10):
    rand.append(random.randint(1,10))

print(selectinon_sort(rand))
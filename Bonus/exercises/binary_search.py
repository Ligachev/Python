def binary_search(list, item):
    '''Бинарный алгоритм поиска'''
    low = 0
    high = len(list)-1
    counter = 0
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        counter+=1
        if guess == item:
            return guess, counter
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

'''поиск произвольного числа из списка'''
import random
rand = random.randint(1,1000000)
my_list = [x for x in range(1000000)]

print(binary_search(my_list, rand))
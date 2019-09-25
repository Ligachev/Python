#проверка простого числа
def is_prime(number):
    if 1<=number<=3:
        return True
    elif number%2==0 or number%3==0:
        return False
    else:
        return True

print(is_prime(abs(int(input('add number: ')))))

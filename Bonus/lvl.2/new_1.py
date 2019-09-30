#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, 
# и возвращающую True, если оно простое, и False - иначе.

def is_prime(number):
    if 1<=number<=3:
        return True
    elif number%2==0 or number%3==0:
        return False
    else:
        return True

print(is_prime(abs(int(input('add number: ')))))

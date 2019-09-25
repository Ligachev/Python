#Модуль числа
def abs(x):
    if x < 0:
        x=-x
        return x
    else:
        return x

print(abs(int(input('add number: '))))
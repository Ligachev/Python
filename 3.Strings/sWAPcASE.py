def swap_case(st):
    new_str=''
    for i in st:
        if 65<=ord(i)<=90:
            new_str+=chr(ord(i)+32)
        elif 97<=ord(i)<=122:
            new_str+=chr(ord(i)-32)
        else:
            new_str+=i
    return new_str

s = input()
result = swap_case(s)
print(result)
def set_operation(arr, count):
    for i in range(count):
        o,*p = list(input().split())
        if o == 'pop':
            s.pop()
        if o == 'remove':
            s.remove(int(p[0]))
        if o == 'discard':
            s.discard(int(p[0]))
    j = 0
    for i in arr:
        j += i
    return j

n = int(input())
s = set(map(int, input().split()))
N = int(input())
print(set_operation(s, N))



'''Тоже самое, но длинее.

def set_operation(arr, arr_command):
    for i in range(len(arr_command)):
        o,*p = arr_command[i]
        if o == 'pop':
            s.pop()
            continue
        if o == 'remove':
            s.remove(int(p[0]))
            continue
        if o == 'discard':
            s.discard(int(p[0]))
            continue
    j = 0
    for i in arr:
        j+=i
    return j

n = int(input())
s = set(map(int, input().split()))
N = int(input())
arr_command = []
for i in range(N):
    arr_command.append(list(input().split()))

print(set_operation(s, arr_command))
'''
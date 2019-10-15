set_A = set(map(int, input().split()))
n = int(input())
list = []
for i in range(n):
    set_B = set(map(int, input().split()))
    if set_A > set_B:
        i = True
        list.append(i)
    else:
        i = False
        list.append(i)
if all(list) == True:
    print(True)
else:
    print(False)
T = int(input())
for i in range(T):
    count_A = int(input())
    set_A = set(map(int, input().split()))
    count_B = int(input())
    set_B = set(map(int, input().split()))
    if set_A < set_B:
        print(True)
    else:
        print(False)
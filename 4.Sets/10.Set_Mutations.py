def set_mutation(set_A, count):
    for i in range(count):
        command, count = list(input().split())
        if command == 'intersection_update':
            set_N = set(map(int, input().split()))
            set_A &= set_N
        if command == 'update':
            set_N = set(map(int, input().split()))
            set_A |= set_N
        if command == 'symmetric_difference_update':
            set_N = set(map(int, input().split()))
            set_A ^= set_N
        if command == 'difference_update':
            set_N = set(map(int, input().split()))
            set_A -= set_N
    return sum(set_A)

A = int(input())
set_A = set(map(int, input().split()))
N = int(input())
print(set_mutation(set_A, N))
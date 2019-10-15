def difference(arg1, arg2):
    arg1 = set(arg1)
    arg2 = set(arg2)
    arg = arg1 ^ arg2
    arg = list(map(int, arg))
    arg.sort()
    for i in arg:
        print(i)

n = int(input())
N = (input().split())

m = int(input())
M = (input().split())

difference(N, M)
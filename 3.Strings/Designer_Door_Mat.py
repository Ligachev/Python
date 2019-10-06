N,M=(input()).split()
N=int(N)
M=int(M)
a='-'
b='.|.'
c=3
d=1
for i in range(N):
    A=''
    if i < N//2:
        length = int((M - c) / 2)
        A=(a*(length))+(b*d)+(a*(length))
        c += 6
        d += 2
        print(A)
    elif i == N//2:
        length = int((M - 7) / 2)
        A=(a*(length))+"WELCOME"+(a*(length))
        print(A)
        c-=6
        d-=2
    elif i > N//2:
        length = int((M - c) / 2)
        A = (a * (length)) + (b * d) + (a * (length))
        c -= 6
        d -= 2
        print(A)
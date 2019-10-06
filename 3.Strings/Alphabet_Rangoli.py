def print_rangoli(size):
    wid=(size*4-3)
    hei=(size*2-1)
    A=[]
    for y in (map(chr, range(ord('a'), 96+size + 1))):
        A.append(y)

    L=[]
    for i in range(hei):
        if i <= int(hei) // 2:
            S = '-'.join(A[i:size])
            L.append(S[::-1]+S[1:])
        elif i > int(hei) // 2:
            S = '-'.join(A[i-(int(hei)//2):size])
            L.insert(0, (S[::-1]+S[1:]))

    a='-'
    on = 0
    for j in L[::-1]:
        string=''
        if on < int(hei) // 2:
            length = int((wid - len(j)) / 2)
            string = (a * length) + j + (a * length)
            print(string)
            on+=1
        elif on == int(hei) // 2:
            length = int((wid - len(j)) / 2)
            string = (a * length) + j + (a * length)
            print(string)
            on += 1
        elif on > int(hei) // 2:
            length = int((wid - len(j)) / 2)
            string = (a * length) + j + (a * length)
            print(string)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

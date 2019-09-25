n=int(input('number of operations: '))
command=[]
fin=[]
for i in range(n):
    command.append(input('add commands: ').split())
for j in command:
    if j[0] == 'insert':
        fin.insert(int(j[1]),int(j[2]))
    elif j[0]=='print':
        print(fin)
    elif j[0]=='remove':
        fin.remove(int(j[1]))
    elif j[0]=='append':
        fin.append(int(j[1]))
    elif j[0]=='sort':
        fin.sort()
    elif j[0]=='reverse':
        fin.reverse()
    elif j[0]=='pop':
        fin.pop()



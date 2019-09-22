students=[]
for a in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
i = 1
while i < len(students):
     for j in range(len(students)-i):
          if students[j][0] > students[j+1][0]:
               students[j], students[j+1] = students[j+1], students[j]
     i += 1

n = 1
while n < len(students):
     for k in range(len(students)-n):
          if students[k][1] < students[k+1][1]:
               students[k], students[k+1] = students[k+1], students[k]
     n += 1

needed=[]
for b in range(len(students)-1, 0, -1):
    if students[b][1] == students[b-1][1]:
        continue
    elif students[b][1] < students[b-1][1] < students[b-2][1]:
        print(students[b-1][0])
        break
    elif students[b][1] < students[b-1][1] == students[b-2][1]:
        needed.append(students[b-1])
        for c in range(len(students)):
            if needed[0][1] == students[c][1]:
                print(students[c][0])
        break
    else:
        print(students[b-1][0])


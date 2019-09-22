n = int(input())
A = input()
A=A.split()
B=[]
p=0
for i in A:
    if int(i) not in B:
        B.append([])
        B[p]=int(i)
        p+=1
k = 1
while k < len(B):
     for j in range(len(B)-k):
          if B[j] > B[j+1]:
               B[j],B[j+1] = B[j+1],B[j]
     k += 1
print(B[-2])
"""
n = int(input())
A = input()
j=0
k=0
for i in A:
    if int(i) > j:
        j=i
for k in A:
    if int(j) > int(k) > int(o):
        o=k
print(o)
"""






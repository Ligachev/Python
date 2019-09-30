#Циклом получить сумму всех элементов списка
#Аналогично, но с использованием другого типа цикла
list=[x+1 for x in range(101)]
j=0
for i in list:
    j+=i
print(j)

j=0
i=0
while i < len(list):
   j+=list[i]
   i+=1
print(j)
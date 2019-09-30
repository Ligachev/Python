#Один из простых вариантов сортировки - сортировка выбором.
#В Python есть готовые функции сортировки. Их использовать нельзя.
#arr = [0,3,24,2,3,7]
#// здесь реализованный алгоритм
#// на выходе должен получится список, содержащий [0, 2, 3, 3, 7, 24]

arr=(str(input('add numbers: '))).split(' ')
for x in range(len(arr)):
    arr[x]=int(arr[x])
i=1
while i < len(arr):
    for j in range(len(arr)-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1]=arr[j+1],arr[j]
    i+=1
print(arr)